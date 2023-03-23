from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
language = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN")))
language.click()


# Finding multiple items from the shop
items =[]
for i in range(1,-1,-1):
    items.append(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, f'productPrice{i}'))))

driver.implicitly_wait(3)

# Clicking the "Big cookie"
for i in range(1000):
    cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
    cookie.click()
    
    # Checking the cookie count
    for item in items:
        cookie_count = driver.find_element(By.XPATH, "(//div[@id='cookies'])[1]")
        current_count = int(cookie_count.text.split(' ')[0])
        price = int(item.text)

        # Checking if there is enough cookies to buy an item
        if current_count > price:
                actions = ActionChains(driver)
                actions.click(item)
                actions.perform()


print(cookie_count.text)
