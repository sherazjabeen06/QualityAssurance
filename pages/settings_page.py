from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SettingsPage(BasePage):
    # Tabs
    MY_PROFILE_TAB = (By.XPATH, "//button[text()='My Profile']")
    COMPANY_TAB = (By.XPATH, "//button[contains(text(),'Company')]")
    API_KEYS_TAB = (By.XPATH, "//button[text()='Api Keys']")

    # My Profile Fields
    NAME_INPUT = (By.NAME, "name")
    DESIGNATION_INPUT = (By.NAME, "designation")
    SAVE_BTN = (By.XPATH, "//button[contains(text(),'save')]")
    
    # Validations
    ERROR_MSG = (By.CLASS_NAME, "error-text") # Hypothetical class based on common UI

    def update_profile(self, name, designation):
        self.click(self.MY_PROFILE_TAB)
        self.type(self.NAME_INPUT, name)
        self.type(self.DESIGNATION_INPUT, designation)
        self.click(self.SAVE_BTN)

    def get_api_keys(self):
        self.click(self.API_KEYS_TAB)
        # Returns a list of text from the 'Key' column
        keys = self.driver.find_elements(By.XPATH, "//table//td[2]")
        return [k.text for k in keys]