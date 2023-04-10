from selenium.webdriver.common.by import By

from pages.base import BasePage

class LoginPage(BasePage):

    login_tab_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/login"]')

    email_login_field_selector = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    password_field_selector = (By.CSS_SELECTOR, 'input[data-qa="login-password"]')
    login_button_selector = (By.CSS_SELECTOR, 'button[data-qa="login-button"]')

    name_signup_field_selector = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    email_signup_field_selector = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    signup_button_selector = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')

    label_existing_user_selector = (By.CSS_SELECTOR, 'form[action="/signup"] p')
    label_incorrect_email_selector = (By.CSS_SELECTOR, 'form[action="/login"] p')

    def login_by_email(self, email, password):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.email_login_field_selector).send_keys(email)
        self.driver.find_element(*self.password_field_selector).send_keys(password)
        self.driver.find_element(*self.login_button_selector).click()

    def register_new_user(self, username, email):
        self.driver.find_element(*self.login_tab_selector).click()
        self.driver.find_element(*self.name_signup_field_selector).send_keys(username)
        self.driver.find_element(*self.email_signup_field_selector).send_keys(email)
        self.driver.find_element(*self.signup_button_selector).click()

    def label_existing_user_is_displayed(self):
        return self.driver.find_element(*self.label_existing_user_selector)

    def label_incorrect_email_is_displayed(self):
        return self.driver.find_element(*self.label_incorrect_email_selector)


