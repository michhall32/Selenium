from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Creating a web driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")


# Handling cookies consent - waiting until the element appears
cookiesConsent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='fc-button fc-cta-consent fc-primary-button']")))
cookiesConsent.click()

# Choosing a language - waiting till the element appears
language_eng = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN")))
language_eng.click()


# Clicking the "Big cookie"
for i in range(300):
    cookie = driver.find_element(By.ID, 'bigCookie')
    cookie.click()


cookie_count = driver.find_element(By.XPATH, "(//div[@id='cookies'])[1]")
print(cookie_count.text)
