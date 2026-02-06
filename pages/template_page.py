from selenium.webdriver.common.by import By
from .base_page import BasePage

class TemplatePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search Templates']")
    ARCHIVED_TAB = (By.XPATH, "//button[contains(text(), 'Archived')]")
    EMPTY_STATE_MSG = (By.XPATH, "//div[contains(@class, 'warning')]") # Yellow box
    BACK_TO_TOP = (By.XPATH, "//*[contains(text(), 'Back to top')]")
    TEMPLATE_CARDS = (By.XPATH, "//h2")

    def search_template(self, name):
        self.enter_text(self.SEARCH_INPUT, name)

    def switch_to_archived(self):
        self.click_element(self.ARCHIVED_TAB)

    def get_empty_state_text(self):
        return self.get_element_text(self.EMPTY_STATE_MSG)

    def click_back_to_top(self):
        self.click_element(self.BACK_TO_TOP)