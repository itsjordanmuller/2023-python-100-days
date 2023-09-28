from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://store.google.com/us/product/pixel_buds_pro?hl=en-US")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
