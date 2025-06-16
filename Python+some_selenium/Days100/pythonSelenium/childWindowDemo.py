import time
from selenium import webdriver
from selenium import ActionChains
from selenium import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()
window_names = driver.window_handles #handles the whole window name in the list

driver.switch_to.window(window_names[1]) #switching the tabs, -> activates the given window in tabs
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() #closes the current opened window

driver.switch_to.window(window_names[0])
assert driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window"

time.sleep(5)