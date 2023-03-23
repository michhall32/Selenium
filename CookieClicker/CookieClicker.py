from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SHOP_ITEMS = 2
COOKIES_CLICKS = 1000

# Getting an amount from the selector
def getCount(selector):
    try:
        result = int(selector.text.split(' ')[0])
        return result
    except:
        return 0

# Waiting for the element to be present on the website
def is_element_present(id_name):
     elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_name)))
     return elem

#Chrome web browser options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#Creating a web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


# Handling cookies consent - waiting until the element appears
cookiesConsent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='fc-button fc-cta-consent fc-primary-button']")))
cookiesConsent.click()

# Choosing a language - waiting till the element appears
language = is_element_present("langSelect-EN")
language.click()


# Finding multiple items from the shop
items =[]
for i in range(SHOP_ITEMS,-1,-1):
    items.append(is_element_present(f'productPrice{i}'))

driver.implicitly_wait(3)


# Clicking the "Big cookie"
for i in range(COOKIES_CLICKS):
    cookie = is_element_present('bigCookie')
    cookie.click()
    cookie_count = driver.find_element(By.ID, "cookies")
    current_count = getCount(cookie_count)


    # Checking if there is enough cookies to buy an item
    for item in items:
        price = getCount(item)

        if current_count >= price and price > 0:
                actions = ActionChains(driver)
                actions.click(item)
                actions.perform()


# Printing the results
for i in range(SHOP_ITEMS):
     item_name = driver.find_element(By.ID, f'productName{i}')
     item_amount = driver.find_element(By.ID, f'productOwned{i}')
     print(f'{item_name.text}: {item_amount.text}')


print(f'\nAmount of cookies left: {cookie_count.text}')