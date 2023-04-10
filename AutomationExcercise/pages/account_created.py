from selenium.webdriver.common.by import By

from pages.base import BasePage


class AccountCreatedPage(BasePage):
    account_created_label_selector = (By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
    continue_button_selector = (By.CSS_SELECTOR, ' a[data-qa="continue-button"]')

    def account_created_label_displayed(self):
        return self.driver.find_element(*self.account_created_label_selector).text

    def continue_to_homepage(self):
        self.driver.find_element(*self.continue_button_selector).click()