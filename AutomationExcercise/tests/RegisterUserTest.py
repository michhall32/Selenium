import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home import HomePage
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.account_created import AccountCreatedPage
from pages.account_deleted import AccountDeletedPage
from utilities.DataGiver import CORRECT_EMAIL, NEW_EMAIL, USERNAME, PASSWORD
from utilities.DataGiver import EMAIL_ALREADY_EXIST_MESSAGE


class RegisterUser(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignupPage(self.driver)
        self.account_created = AccountCreatedPage(self.driver)
        self.account_deleted = AccountDeletedPage(self.driver)

    def test_register_new_user(self):
        # self.home_page.navigate_to_homepage()
        # button_color = self.home_page.get_button_color()
        # self.assertEqual(button_color, 'orange')

        self.login_page.register_new_user(USERNAME, NEW_EMAIL)
        self.signup_page.enter_account_information(PASSWORD)
        self.signup_page.select_birth_date()
        self.signup_page.enter_address_information("Harry", "Potter", 'Hogwarts')
        account_created = self.account_created.account_created_label_displayed()
        self.assertEqual(account_created, 'ACCOUNT CREATED!')

        self.account_created.continue_to_homepage()
        self.driver.refresh()
        self.account_created.continue_to_homepage()
        logged_user_label = self.home_page.username_is_displayed()
        self.assertEqual(logged_user_label, USERNAME)

        self.home_page.delete_account()
        account_deleted = self.account_deleted.account_deleted_label_displayed()
        self.assertEqual(account_deleted, 'ACCOUNT DELETED!')

        self.account_deleted.continue_to_homepage()

    def test_register_existing_user(self):
        self.login_page.register_new_user(USERNAME, CORRECT_EMAIL)
        existing_user_label = self.login_page.label_existing_user_is_displayed().text
        self.assertEqual(existing_user_label, EMAIL_ALREADY_EXIST_MESSAGE)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
