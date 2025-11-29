from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchasePage:
    """
    Purchase / checkout page.

    Assumed elements:
      - First name: id='firstName'
      - Last name: id='lastName'
      - Email: id='email'
      - Phone: id='phone'
      - Confirm button: id='confirmPurchase'
      - Status label: id='orderStatus'  (text must contain 'PendingCapture')
      - Total price: id='totalPrice'    (e.g. '$123.45')
    """

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    CONFIRM_BUTTON = (By.ID, "confirmPurchase")
    STATUS_LABEL = (By.ID, "orderStatus")
    PRICE_LABEL = (By.ID, "totalPrice")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_details(self, name: str, email: str, phone: str):
        """Fill passenger details using dummy/random user data."""
        parts = name.split(" ", 1)
        first = parts[0]
        last = parts[1] if len(parts) > 1 else "Test"

        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PHONE)).send_keys(phone)

    def confirm(self):
        """Click confirm/purchase button."""
        btn = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
        btn.click()

    def validate_status_pending_capture(self):
        """Assert that order status contains 'PendingCapture'."""
        text = self.wait.until(
            EC.visibility_of_element_located(self.STATUS_LABEL)
        ).text
        assert "PendingCapture" in text, f"Expected 'PendingCapture' in status, got: {text}"

    def validate_price_greater_than_100(self):
        """Assert that total price > 100.00."""
        text = self.wait.until(
            EC.visibility_of_element_located(self.PRICE_LABEL)
        ).text

        # Extract numeric part from something like '$123.45'
        amount_str = "".join(c for c in text if c.isdigit() or c == ".")
        if not amount_str:
            raise AssertionError(f"Could not parse price from: {text}")

        amount = float(amount_str)
        assert amount > 100.0, f"Expected price > 100, got {amount}"
