import pytest
from pages.qlibrary_page import QLibraryPage

def test_duplicate_warning_bug(driver):
    """TC_QL_04: Verify no duplicate test names in impact modal (BUG_QL_01)"""
    ql = QLibraryPage(driver)
    driver.get("https://app.hyrenet.in/library")
    
    ql.start_edit_flow()
    warning_text = ql.get_warning_message()
    
    # Check for duplicate "Webdevelopment" in the warning string
    count = warning_text.count("Webdevelopment")
    assert count == 1, f"BUG FOUND: Duplicate test names found in impact modal. Count: {count}"

def test_bulk_import_validation(driver):
    """TC_QL_07: Verify import modal is accessible"""
    ql = QLibraryPage(driver)
    ql.open_import_modal()
    # Check if the upload area is present
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'Supported formats: CSV')]")