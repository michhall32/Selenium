from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import random

from pages.base import BasePage


class SignupPage(BasePage):
    radio_button_selector = (By.ID, 'id_gender1')
    password_field_selector = (By.CSS_SELECTOR, 'input[data-qa="password"')

    random_days_selector = (By.CSS_SELECTOR, 'select[data-qa="days"]')
    random_month_selector = (By.CSS_SELECTOR, f'select[data-qa="months"] option[value="{random.randint(1, 12)}"]')
    random_year_selector = (By.CSS_SELECTOR, f'select[data-qa="years"] option[value="{random.randint(1900, 2021)}"]')

    newsletter_checkbox_selector = (By.ID, 'newsletter')
    offers_checkbox_selector = (By.ID, 'optin')

    first_name_selector = (By.CSS_SELECTOR, 'input[data-qa="first_name"]')
    last_name_selector = (By.CSS_SELECTOR, 'input[data-qa="last_name"]')
    address_selector = (By.CSS_SELECTOR, 'input[data-qa="address"]')
    country_selector = (By.CSS_SELECTOR, 'select[data-qa="country"]')
    state_selector = (By.CSS_SELECTOR, 'input[data-qa="state"]')
    city_selector = (By.CSS_SELECTOR, 'input[data-qa="city"]')
    zipcode_selector = (By.CSS_SELECTOR, 'input[data-qa="zipcode"]')
    mobile_number_selector = (By.CSS_SELECTOR, 'input[data-qa="mobile_number"]')
    create_account_button_selector = (By.CSS_SELECTOR, 'button[data-qa="create-account"]')

    def enter_account_information(self, password):
        self.driver.find_element(*self.radio_button_selector).click()
        self.driver.find_element(*self.password_field_selector).send_keys(password)

    def select_birth_date(self):
        day = Select(self.driver.find_element(*self.random_days_selector))
        day.select_by_value(str(random.randint(1, 30)))
        self.driver.find_element(*self.random_month_selector).click()
        self.driver.find_element(*self.random_year_selector).click()

    def enter_address_information(self, first_name, last_name, city):
        self.driver.find_element(*self.newsletter_checkbox_selector).click()
        self.driver.find_element(*self.offers_checkbox_selector).click()
        self.driver.find_element(*self.first_name_selector).send_keys(first_name)
        self.driver.find_element(*self.last_name_selector).send_keys(last_name)
        self.driver.find_element(*self.address_selector).send_keys(f"pacanowo random {random.randint(1, 100)}")
        country = Select(self.driver.find_element(*self.country_selector))
        country.select_by_index(random.randint(0, 6))
        self.driver.find_element(*self.state_selector).send_keys("podkarpacie")
        self.driver.find_element(*self.city_selector).send_keys(city)
        self.driver.find_element(*self.zipcode_selector).send_keys('2137')
        self.driver.find_element(*self.mobile_number_selector).send_keys('111-111-111')
        self.driver.find_element(*self.create_account_button_selector).click()
