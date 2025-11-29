from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """
    Home / Flights search page.

    Assumed elements:
      - One-way radio: id='oneWay'
      - From input: id='fromCity'
      - To input: id='toCity'
      - Search button: id='searchButton'
    """

    BASE_URL = "https://example-flight-site.com"  # <-- change to real URL

    ONE_WAY_RADIO = (By.ID, "oneWay")
    FROM_INPUT = (By.ID, "fromCity")
    TO_INPUT = (By.ID, "toCity")
    SEARCH_BUTTON = (By.ID, "searchButton")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # -------- navigation --------

    def open(self):
        """Open home / search page."""
        self.driver.get(self.BASE_URL)
        self.driver.maximize_window()

    # -------- actions --------

    def select_one_way(self):
        """Select 'One-way' trip type."""
        one_way = self.wait.until(EC.element_to_be_clickable(self.ONE_WAY_RADIO))
        one_way.click()

    def _type_and_choose_city(self, locator, city: str):
        """
        Type city name and choose first suggestion via ArrowDown+Enter.
        Adjust if site uses simple text inputs only.
        """
        field = self.wait.until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(city)

        # If there is an autosuggest dropdown, this picks first option.
        field.send_keys(Keys.ARROW_DOWN)
        field.send_keys(Keys.ENTER)

    def enter_from(self, city: str):
        """Fill 'From' city."""
        self._type_and_choose_city(self.FROM_INPUT, city)

    def enter_to(self, city: str):
        """Fill 'To' city."""
        self._type_and_choose_city(self.TO_INPUT, city)

    def click_search(self):
        """Click search button."""
        btn = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        btn.click()
