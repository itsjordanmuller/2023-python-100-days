from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/selenium/")

pip_install_cmd = driver.find_element(By.CSS_SELECTOR, "span#pip-command")
package_desc = driver.find_element(By.CSS_SELECTOR, "section#introduction p")
release_date = driver.find_element(By.CSS_SELECTOR, ".package-header__date")

print(f"CMD\t{pip_install_cmd.text}")
print(f"DESC\t{package_desc.text}")
print(f"DATE\t{release_date.text}")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
