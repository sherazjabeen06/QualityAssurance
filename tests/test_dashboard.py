import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage # Assuming you have the login code from earlier

def test_dashboard_components_visibility(driver):
    """TC_DB_01 & TC_DB_07: Verify Dashboard components and License display"""
    dashboard = DashboardPage(driver)
    
    # Prerequisite: Already logged in
    assert dashboard.is_dashboard_loaded(), "Dashboard failed to load"
    
    # Verify License Data
    license_text = dashboard.get_license_status()
    assert "1 / 100" in license_text, f"License mismatch: {license_text}"
    print(f"Verified License: {license_text}")

def test_calendar_month_display(driver):
    """TC_DB_02: Verify current month on Calendar"""
    dashboard = DashboardPage(driver)
    
    month_year = dashboard.get_current_calendar_month()
    assert "February 2026" in month_year, f"Wrong month displayed: {month_year}"

def test_sidebar_navigation(driver):
    """TC_DB_06: Verify navigation to QLibrary via sidebar"""
    dashboard = DashboardPage(driver)
    
    dashboard.click_element(dashboard.QLIBRARY_MENU)
    # Verify URL change or page heading
    assert "library" in driver.current_url.lower()