from selenium.webdriver.common.by import By
import random

from pages.base import BasePage


class ProductsPage(BasePage):
    products_tab_selector = (By.CSS_SELECTOR, '.shop-menu a[href="/products"]')
    brands_button_selector = (By.CSS_SELECTOR, '.brands-name span')
    products_items_selector = (By.CSS_SELECTOR, '.single-products')

    def close_ad(self):
        self.driver.find_element(*self.products_tab_selector).click()
        self.driver.refresh()

    def navigate_to_products(self):
        self.driver.find_element(*self.products_tab_selector).click()

    def list_of_brands(self):
        return self.driver.find_elements(*self.brands_button_selector)

    def number_of_items(self, brand_element):
        number_of_items = int(brand_element.text.strip('()'))
        brand_element.click()
        return number_of_items

    def get_amount_of_visible_products(self):
        products = self.driver.find_elements(*self.products_items_selector)
        return len(products)
