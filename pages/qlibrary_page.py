from selenium.webdriver.common.by import By
from .base_page import BasePage

class QLibraryPage(BasePage):
    # Locators
    IMPORT_BTN = (By.XPATH, "//button[contains(., 'Import Questions')]")
    EDIT_ICON = (By.XPATH, "(//i[contains(@class, 'edit') or @data-icon='edit'])[1]") # Adjust based on actual tag
    PROCEED_BTN = (By.XPATH, "//button[text()='Proceed']")
    DIFFICULTY_DROPDOWN = (By.XPATH, "//div[contains(@class, 'select')]") # MCQ Modal
    UPDATE_BTN = (By.XPATH, "//button[text()='Update']")
    MODAL_WARNING_TEXT = (By.XPATH, "//div[contains(@class, 'modal')]//p")

    def open_import_modal(self):
        self.click_element(self.IMPORT_BTN)

    def start_edit_flow(self):
        # This triggers the BUG_QL_01 check
        self.click_element(self.EDIT_ICON)

    def get_warning_message(self):
        return self.get_element_text(self.MODAL_WARNING_TEXT)