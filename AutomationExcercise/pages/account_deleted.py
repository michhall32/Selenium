from selenium.webdriver.common.by import By

from pages.base import BasePage

class AccountDeletedPage(BasePage):

    account_deleted_label_selector = (By.CSS_SELECTOR, 'h2[data-qa="account-deleted"]')
    continue_button_selector = (By.CSS_SELECTOR, ' a[data-qa="continue-button"]')

    def account_deleted_label_displayed(self):
        return self.driver.find_element(*self.account_deleted_label_selector).text

    def continue_to_homepage(self):
        self.driver.find_element(*self.continue_button_selector).click()