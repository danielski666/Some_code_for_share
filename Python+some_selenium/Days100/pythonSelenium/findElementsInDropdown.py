import time

from selenium import webdriver
from selenium import By
from selenium.webdriver.support import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID, "autosuggest")).text -> will not work with the dynamic parts of website
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(10)