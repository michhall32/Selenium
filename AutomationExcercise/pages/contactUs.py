from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ContactUsPage(BasePage):
    contactUs_button_selector = (By.CSS_SELECTOR, '.shop-menu  a[href="/contact_us"]')
    getintouch_label_selector = (By.CSS_SELECTOR, '.contact-form h2')
    name_field_selector = (By.CSS_SELECTOR, 'input[data-qa="name"]')
    email_field_selector = (By.CSS_SELECTOR, 'input[data-qa="email"]')
    subject_field_selector = (By.CSS_SELECTOR, 'input[data-qa="subject"]')
    message_field_selector = (By.CSS_SELECTOR, 'textarea[data-qa="message"]')

    choose_file_selector = (By.CSS_SELECTOR, 'input[type="file"]')
    submit_button_selector = (By.CSS_SELECTOR, 'input[data-qa="submit-button"]')
    success_message_selector = (By.CSS_SELECTOR, 'div[class="status alert alert-success"]')
    home_button_selector = (By.CSS_SELECTOR, 'a[class="btn btn-success"]')

    def navigate_to_contact(self):
        self.driver.find_element(*self.contactUs_button_selector).click()

    def getintouch_label_displayed(self):
        return self.driver.find_element(*self.getintouch_label_selector).text

    def fill_form(self, name, email, subject, message):
        self.driver.find_element(*self.name_field_selector).send_keys(name)
        self.driver.find_element(*self.email_field_selector).send_keys(email)
        self.driver.find_element(*self.subject_field_selector).send_keys(subject)
        self.driver.find_element(*self.message_field_selector).send_keys(message)

    def upload_file(self, file_path):
        self.driver.find_element(*self.choose_file_selector).send_keys(file_path)

    def submit_form(self):
        self.driver.find_element(*self.submit_button_selector).click()

    def window_alert(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()

    def success_message(self):
        return self.driver.find_element(*self.success_message_selector).text

    def back_to_home(self):
        self.driver.find_element(*self.home_button_selector).click()
