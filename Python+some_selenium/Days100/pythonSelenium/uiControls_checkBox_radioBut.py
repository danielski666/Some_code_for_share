import time


from selenium import webdriver
from selenium import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

check_boxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
for box in check_boxes:
    if box.get_attribute("value") == "option2":
        box.click()
        assert box.is_selected(), "Box should be selected but it is not."
        break

radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
for radiobutton in radio_buttons:
    if radiobutton.get_attribute('value') == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected(), "radio2 is not selected"
        break

#if you know that the poition shouldnt change e.g from requirements, pos. is constance
radiobuttonssecond = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttonssecond[1].click()
assert radiobuttonssecond[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(3)