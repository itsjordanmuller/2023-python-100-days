from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

pkg = input("Enter a project name from PyPI.org:\n")
print(pkg)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://pypi.org/project/" + pkg + "/")

package_name = driver.find_element(By.CSS_SELECTOR, ".package-header__name")
pip_install_cmd = driver.find_element(By.CSS_SELECTOR, "#pip-command")
release_date = driver.find_element(By.CSS_SELECTOR, ".package-header__date")
package_desc = driver.find_element(By.CSS_SELECTOR, ".package-description__summary")

print(f"NAME\t{package_name.text}")
print(f"CMD\t{pip_install_cmd.text}")
print(f"DATE\t{release_date.text}")
print(f"DESC\t{package_desc.text}")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
