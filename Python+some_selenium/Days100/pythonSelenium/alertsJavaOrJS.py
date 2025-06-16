import time


from selenium import webdriver
from selenium import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("Rahul")
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert alertText == "Hello Rahul, share this practice page and share your knowledge"
alert.accept()
#alert.dismiss() -> for the cancelation of the confirmation popup

time.sleep(5)