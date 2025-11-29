import random
import pytest
from selenium.common.exceptions import InvalidSessionIdException, NoSuchWindowException

from utilities.driver_factory import DriverFactory
from utilities.data_generator import random_user
from pages.home_page import HomePage
from pages.flights_page import FlightsPage
from pages.purchase_page import PurchasePage


CITIES = ["Boston", "Berlin", "Paris", "Buenos Aires", "Dubai", "Tokyo"]


def purchaseEndToEnd(deptCity=None, desCity=None, flightSeq=None):
    """
    Generic 'Purchase Flight' flow for any flight website.

    Optional params:
      - deptCity (str)
      - desCity (str)
      - flightSeq (int): 3 => 3rd flight

    Requirements covered:
      1) Input correct flight data and select correct flight sequence.
      2) Make purchase with dummy user data each time.
      3) Validate:
           - Status == 'PendingCapture'
           - Price > 100.00
      4) If validation fails, stop and show reason in logs.
      5) Sanitize inputs and raise for wrong types.
    """

    # ----- input sanitization -----
    if deptCity is not None and not isinstance(deptCity, str):
        raise Exception("deptCity must be a string")
    if desCity is not None and not isinstance(desCity, str):
        raise Exception("desCity must be a string")
    if flightSeq is not None and not isinstance(flightSeq, int):
        raise Exception("flightSeq must be an integer")

    driver = DriverFactory.get_driver()

    try:
        dept = deptCity or random.choice(CITIES)
        dest = desCity or random.choice(CITIES)

        if flightSeq is None:
            seq = random.randint(1, 3)
        elif flightSeq <= 0:
            # Assignment says: wrong flightSeq → still run, but our code adjusts.
            seq = 1
        else:
            seq = flightSeq

        print("\n" + "=" * 70)
        print(f"RUN: {dept}  →  {dest}  (flightSeq = {seq})")
        print("=" * 70)

        # ---------- Page objects ----------
        home = HomePage(driver)
        flights_page = FlightsPage(driver)
        purchase_page = PurchasePage(driver)

        # 1) Open site
        print("[1] Opening home page ...")
        home.open()

        # 2) Select One‑way + search for flight
        print("[2] Selecting 'One-way' trip type ...")
        home.select_one_way()

        print(f"[3] Entering From = {dept} ...")
        home.enter_from(dept)

        print(f"[4] Entering To = {dest} ...")
        home.enter_to(dest)

        print("[5] Clicking Search ...")
        home.click_search()

        # 3) Select correct flight sequence
        print(f"[6] Selecting flight #{seq} from results ...")
        flights_page.select_flight(seq)

        # 4) Make purchase with random user
        user = random_user()
        print(f"[7] Filling passenger details: {user['name']} / {user['email']} ...")
        purchase_page.fill_details(user["name"], user["email"], user["phone"])

        print("[8] Confirming purchase ...")
        purchase_page.confirm()

        # 5) Validations
        print("[9] Validating status 'PendingCapture' ...")
        purchase_page.validate_status_pending_capture()
        print("    ✔ Status validation PASSED")

        print("[10] Validating price > 100.00 ...")
        purchase_page.validate_price_greater_than_100()
        print("    ✔ Price validation PASSED")

        print("=" * 70)
        print("✔ purchaseEndToEnd COMPLETED SUCCESSFULLY")
        print("=" * 70)

    except (InvalidSessionIdException, NoSuchWindowException) as e:
        print("❌ Browser/Session error:", e)
        raise
    except AssertionError as e:
        print("❌ VALIDATION FAILED:", e)
        raise
    except Exception as e:
        print("❌ UNEXPECTED ERROR:", e)
        raise
    finally:
        try:
            driver.quit()
        except Exception:
            pass


# ---------- Required 5 test executions ----------

def test_case_1():
    # 1. Boston, Berlin, 2
    purchaseEndToEnd("Boston", "Berlin", 2)


def test_case_2():
    # 2. All parameters random
    purchaseEndToEnd()


def test_case_3():
    # 3. Boston, Boston, 1
    purchaseEndToEnd("Boston", "Boston", 1)


def test_case_4():
    # 4. Paris, Berlin, 0 (invalid seq → defaults to 1)
    purchaseEndToEnd("Paris", "Berlin", 0)


def test_case_5():
    # 5. Custom
    purchaseEndToEnd("Dubai", "Tokyo", 3)
