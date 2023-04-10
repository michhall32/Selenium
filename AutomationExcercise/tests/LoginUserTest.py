import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities.DataGiver import CORRECT_EMAIL, INCORRECT_EMAIL, USERNAME, PASSWORD
from utilities.DataGiver import INCORRECT_LOGIN_MESSAGE

from pages.login import LoginPage
from pages.home import HomePage


class LoginUser(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_login_with_correct_email(self):
        self.login_page.login_by_email(CORRECT_EMAIL, PASSWORD)
        self.assertTrue(self.home_page.username_is_displayed())
        logged_user_label = self.home_page.username_is_displayed()
        self.assertEqual(logged_user_label, USERNAME)

    def test_login_with_incorrect_email(self):
        self.login_page.login_by_email(INCORRECT_EMAIL, PASSWORD)
        incorrect_email_label = self.login_page.label_incorrect_email_is_displayed().text
        self.assertEqual(incorrect_email_label, INCORRECT_LOGIN_MESSAGE)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
