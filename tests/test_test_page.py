import pytest
from pages.test_page import TestPage

def test_search_functionality(driver):
    """TC_TM_01: Verify search filters tests correctly"""
    test_page = TestPage(driver)
    driver.get("https://app.hyrenet.in/test") # Replace with actual navigation
    
    test_page.search_for_test("Java")
    assert "Java" in test_page.get_first_test_name(), "Search results mismatch"

def test_epoch_date_bug(driver):
    """TC_TM_06: Check for the 1970 date bug (Data Integrity)"""
    test_page = TestPage(driver)
    
    is_clean = test_page.verify_date_not_epoch()
    if not is_clean:
        pytest.fail("BUG FOUND: Test card displaying Unix Epoch date (Jan 1, 1970)")

def test_create_test_navigation(driver):
    """TC_TM_03: Verify 'Create Test' button works"""
    test_page = TestPage(driver)
    test_page.click_create_test()
    assert "create" in driver.current_url.lower()