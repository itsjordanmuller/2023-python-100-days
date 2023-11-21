import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = 0
# goal = 100

milliseconds_between_clicks = 1

while True:
    cookie.click()

    time.sleep(milliseconds_between_clicks / 1000)

    store_items = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
    for item in store_items:
        try:
            item.click()
        except Exception as e:
            print(f"Could not click the item: {e}")
            pass

    money_element = driver.find_element(By.CSS_SELECTOR, "div#money")
    money = float(money_element.text.replace(",", "").split()[0])

print(f"Final Money: {money}")
