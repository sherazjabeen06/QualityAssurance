import pytest
from pages.template_page import TemplatePage

def test_archived_tab_message_bug(driver):
    """TC_TP_03: Check for the incorrect wording bug (BUG_TP_02)"""
    template_page = TemplatePage(driver)
    driver.get("https://app.hyrenet.in/templates")
    
    template_page.switch_to_archived()
    msg = template_page.get_empty_state_text()
    
    # This will fail and report the bug
    assert "templates" in msg.lower(), f"BUG FOUND: Archive message uses 'tests' instead of 'templates'. Actual: {msg}"

def test_duplicate_cards(driver):
    """TC_TP_01: Automated check for duplicate template names (BUG_TP_01)"""
    template_page = TemplatePage(driver)
    cards = driver.find_elements(By.TAG_NAME, "h2")
    names = [card.text for card in cards if card.text != ""]
    
    assert len(names) == len(set(names)), f"BUG FOUND: Duplicate templates detected: {names}"