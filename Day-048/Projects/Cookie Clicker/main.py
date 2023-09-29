import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
money = 0
goal = 100

milliseconds_between_clicks = 10

while True:
    cookie.click()

    time.sleep(milliseconds_between_clicks / 1000)

    money_element = driver.find_element(By.CSS_SELECTOR, "div#money")
    money = float(money_element.text.replace(",", "").split()[0])

    if money >= (goal - 1):
        print("Money reached 100 or more. Stopping the clicks.")
        break

print(f"Final Money: {money}")
