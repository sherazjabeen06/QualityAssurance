from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators (Based on standard naming conventions)
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.signin_button = (By.XPATH, "//button[contains(text(), 'Sign-in')]")
        self.password_toggle = (By.CSS_SELECTOR, ".relative svg") # The eye icon

    def enter_credentials(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signin(self):
        self.driver.find_element(*self.signin_button).click()

    def toggle_password(self):
        self.driver.find_element(*self.password_toggle).click()