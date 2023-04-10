import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.products import ProductsPage


class ProductsFilters(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(4)
        self.driver.get('https://automationexercise.com/')

        self.products_page = ProductsPage(self.driver)

        self.products_page.close_ad()

    def test_brands(self):
        self.products_page.navigate_to_products()
        brands_elements = self.products_page.list_of_brands()
        error_log = []

        for i in range(len(brands_elements)):
            try:
                brand_element = self.products_page.list_of_brands()[i]
                expected_number_of_products = self.products_page.number_of_items(brand_element)
                actual_number_of_products = self.products_page.get_amount_of_visible_products()
                self.assertEqual(expected_number_of_products, actual_number_of_products)
            except AssertionError as e:
                error = f'Element no. {i + 1} from the list failed. More details: {e}'
                error_log.append(error)
                continue

        self.assertTrue(error_log == [], '\n' + '\n'.join(error_log))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
