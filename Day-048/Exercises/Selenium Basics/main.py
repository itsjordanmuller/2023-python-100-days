from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/selenium/")

pip_install_cmd = driver.find_element(By.CSS_SELECTOR, "span#pip-command")

print(pip_install_cmd, type(pip_install_cmd))

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
