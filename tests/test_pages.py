import pytest
from pages.custom_pages import CustomPages

def test_cta_toggle_visibility(driver):
    """TC_PG_03: Verify CTA sub-fields appear on toggle"""
    pg = CustomPages(driver)
    driver.get("https://app.hyrenet.in/pages")
    
    pg.click_element(pg.TEST_END_PAGE_EDIT)
    # Toggle it ON
    pg.toggle_cta()
    
    # Assert CTA fields are now visible
    assert pg.is_cta_label_visible(), "BUG: CTA Label field did not appear after toggle"

def test_mandatory_heading_validation(driver):
    """TC_PG_02: Verify heading cannot be empty"""
    pg = CustomPages(driver)
    pg.open_login_edit()
    
    pg.update_page_heading("") # Empty string
    
    # Check for HTML5 validation or error message
    error = driver.find_element(By.XPATH, "//*[contains(text(), 'required')]")
    assert error.is_displayed()