import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://app.hyrenet.in/")
    
    login_page.enter_credentials("hyrenet+bugathon@guvi.in", "hyrenettest@123")
    login_page.click_signin()
    
    # Assert Dashboard URL or Element
    assert "dashboard" in driver.current_url.lower()

def test_invalid_email_format(driver):
    login_page = LoginPage(driver)
    driver.get("https://app.hyrenet.in/")
    
    login_page.enter_credentials("invalid_email@", "password123")
    login_page.click_signin()
    
    # You would look for an error message element here
    # error = driver.find_element(By.ID, "error-msg").text
    # assert "Invalid email" in error