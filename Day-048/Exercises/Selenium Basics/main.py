from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

pkg = input("Enter a project name from PyPI.org:\n")
print(pkg)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/" + pkg + "/")

pip_install_cmd = driver.find_element(By.CSS_SELECTOR, "#pip-command")
package_name = driver.find_element(By.CSS_SELECTOR, ".package-header__name")
release_date = driver.find_element(By.CSS_SELECTOR, ".package-header__date")

print(f"NAME\t{package_name.text}")
print(f"CMD\t{pip_install_cmd.text}")
print(f"DATE\t{release_date.text}")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
