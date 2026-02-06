from selenium.webdriver.common.by import By
from .base_page import BasePage

class CustomPages(BasePage):
    # Locators
    LOGIN_PAGE_EDIT = (By.XPATH, "//h2[text()='Login Page']/following-sibling::button")
    TEST_END_PAGE_EDIT = (By.XPATH, "//h2[text()='Test End Page']/following-sibling::button")
    
    HEADING_INPUT = (By.NAME, "heading")
    CONTENT_INPUT = (By.NAME, "content")
    CTA_TOGGLE = (By.XPATH, "//span[contains(text(), 'Enable CTA')]/preceding-sibling::input")
    UPDATE_BTN = (By.XPATH, "//button[text()='Update']")

    def open_login_edit(self):
        self.click_element(self.LOGIN_PAGE_EDIT)

    def update_page_heading(self, text):
        # Clears and types new heading
        element = self.wait_for_element(self.HEADING_INPUT)
        element.clear()
        element.send_keys(text)
        self.click_element(self.UPDATE_BTN)

    def toggle_cta(self):
        self.click_element(self.CTA_TOGGLE)

    def is_cta_label_visible(self):
        return self.driver.find_element(By.NAME, "ctaLabel").is_displayed()