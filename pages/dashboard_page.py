from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    # Sidebar Locators
    DASHBOARD_MENU = (By.XPATH, "//span[text()='Dashboard']")
    TEST_MENU = (By.XPATH, "//span[text()='Test']")
    QLIBRARY_MENU = (By.XPATH, "//span[text()='My QLibrary']")
    
    # Dashboard Component Locators
    VISIT_SUMMARY_HEADER = (By.XPATH, "//h2[text()='Users Visit Summary']")
    CALENDAR_MONTH = (By.XPATH, "//div[contains(@class, 'calendar')]//h2")
    LICENSE_INFO = (By.XPATH, "//div[contains(text(), 'License')]")
    VIEW_REPORT_BTNS = (By.XPATH, "//button[contains(., 'view report')]")

    def is_dashboard_loaded(self):
        return self.wait_for_element(self.VISIT_SUMMARY_HEADER).is_displayed()

    def navigate_to_test_section(self):
        self.click_element(self.TEST_MENU)

    def get_license_status(self):
        return self.get_element_text(self.LICENSE_INFO)

    def get_current_calendar_month(self):
        return self.get_element_text(self.CALENDAR_MONTH)