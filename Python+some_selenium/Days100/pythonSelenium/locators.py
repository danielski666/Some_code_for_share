import time

from selenium import webdriver
from selenium import By
from selenium.webdriver.support import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# ID, Xpath, CSSSelector, Classname, name, linkText - to find out the elements on the page

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("0123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -> //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -> tagname[attribute='value'] -> input[type='submit'], by ID in CSS: #id -> #inlineRadio1, by CLASS_NAME: .classname -> .alert-success
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Maurice")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#dropdown menu to handle use Select()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(5)
dropdown.select_by_index(0)
#dropdown.select_by_value("<value>") -> can be used if exists

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear() #for clear the text boxes and other things

time.sleep(10)