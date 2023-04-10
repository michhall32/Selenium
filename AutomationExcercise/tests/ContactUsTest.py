import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.contactUs import ContactUsPage
from pages.home import HomePage
from utilities.DataGiver import getRandomData
from utilities.DataGiver import CONTACT_US_SUCCESS_MESSAGE, FILE_PATH, CORRECT_EMAIL

class ContactUsForm(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.contactUs_page = ContactUsPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_contact_form_correct_email(self):
        self.contactUs_page.navigate_to_contact()
        self.assertTrue(self.contactUs_page.getintouch_label_displayed())
        self.contactUs_page.fill_form(getRandomData(6), CORRECT_EMAIL, getRandomData(40), getRandomData(250))
        self.contactUs_page.upload_file(FILE_PATH)
        self.contactUs_page.submit_form()
        self.contactUs_page.window_alert()
        self.assertEqual(CONTACT_US_SUCCESS_MESSAGE, self.contactUs_page.success_message())

        # self.contactUs_page.back_to_home()            #TODO AD BLOCKS THE PAGE --> FIGURE OUT HOW TO CLOSE AD
        # self.driver.refresh()
        # self.contactUs_page.back_to_home()
        # button_color = self.home_page.get_button_color()
        # self.assertEqual('orange', button_color)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
