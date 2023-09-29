from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
maintainers = driver.find_elements(
    By.CSS_SELECTOR, "span.sidebar-section__user-gravatar-text"
)

maintainer_texts = [
    maintainer.text for maintainer in maintainers[: len(maintainers) // 2]
]

copy_btn = driver.find_element(
    By.CSS_SELECTOR, ".package-header__pip-instructions button"
)

copy_btn.click()

search = driver.find_element(By.CSS_SELECTOR, "input#search")
search.send_keys({package_name.text})
search.send_keys(Keys.ENTER)

print(f"NAME\t{package_name.text}")
print(f"CMD\t{pip_install_cmd.text}")
print(f"DATE\t{release_date.text}")
print(f"DESC\t{package_desc.text}")
print(f"PPL\t{', '.join(maintainer_texts)}")

# Close a Tab
# driver.close()

# Close Entire Instance
# driver.quit()
