from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlightsPage:
    """
    Flights results page.

    Assumed elements:
      - Each result card: css '.flight-card'
      - Inside card, 'select' button: css '.select-flight'
    """

    FLIGHT_CARDS = (By.CSS_SELECTOR, ".flight-card")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_flight(self, seq: int = 1):
        """
        Select the seq-th (1-based) flight result.
        Raises informative exception if index is invalid.
        """
        cards = self.wait.until(
            EC.presence_of_all_elements_located(self.FLIGHT_CARDS)
        )

        if not cards:
            raise Exception("No flight results found")

        index = max(0, seq - 1)
        if index >= len(cards):
            raise Exception(
                f"Flight index {seq} not found. Total available: {len(cards)}"
            )

        card = cards[index]
        button = card.find_element(By.CSS_SELECTOR, ".select-flight")
        button.click()
