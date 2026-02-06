import pytest
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage

class TestSettings:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)
        
        # Initial login to reach dashboard
        self.driver.get("https://app.hyrenet.in/login")
        self.login_page.login("hyrenet+bugathon@guvi.in", "password123")
        self.driver.get("https://app.hyrenet.in/settings")

    def test_tc_st_01_update_profile_success(self):
        """Verify user can update profile details"""
        self.settings_page.update_profile("Reddy QA", "Automation Lead")
        # Validation: Check if a success toast or header change appears
        # assert "Reddy QA" in self.settings_page.get_header_name()

    def test_tc_st_02_profile_validation(self):
        """Verify error message when Name is empty"""
        self.settings_page.update_profile("", "Tester")
        error = self.settings_page.get_text(self.settings_page.ERROR_MSG)
        assert "Name is required" in error

    def test_tc_st_06_api_key_masking(self):
        """Verify API keys are masked with 'x'"""
        keys = self.settings_page.get_api_keys()
        for key in keys:
            assert "xxxx" in key, f"Key {key} is not properly masked!"