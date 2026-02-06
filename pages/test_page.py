from selenium.webdriver.common.by import By
from .base_page import BasePage

class TestPage(BasePage):
    # Locators
    CREATE_TEST_BTN = (By.XPATH, "//button[contains(., 'Create Test')]")
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search Tests']")
    TEST_CARDS = (By.XPATH, "//div[contains(@class, 'card')]")
    TEST_NAMES = (By.TAG_NAME, "h2") # Or the specific class for test names
    COPY_LINK_ICON = (By.XPATH, "(//button[contains(@class, 'copy')])[1]")

    def search_for_test(self, test_name):
        self.enter_text(self.SEARCH_BAR, test_name)

    def get_first_test_name(self):
        return self.get_element_text(self.TEST_NAMES)

    def click_create_test(self):
        self.click_element(self.CREATE_TEST_BTN)

    def verify_date_not_epoch(self):
        # This automated check finds BUG_TM_01
        dates = self.driver.find_elements(By.XPATH, "//*[contains(text(), '1970')]")
        return len(dates) == 0