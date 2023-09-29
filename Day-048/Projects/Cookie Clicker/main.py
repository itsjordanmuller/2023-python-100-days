from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(By.CSS_SELECTOR, "div#money").text
cookie = driver.find_element(By.CSS_SELECTOR, "div#cookie")

print(f"MONEY\t{money}")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
