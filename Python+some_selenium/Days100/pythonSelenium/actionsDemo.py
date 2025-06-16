import time
from selenium import webdriver
from selenium import ActionChains
from selenium import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

action = ActionChains(driver)
#action.double_click(driver.find_element(By....))
#action.context_click(...) -> to make a right click
#action.drag_and_drop(...)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


time.sleep(5)

# projekt.pociagdokariery.pl
# Baza usług rozwojowych, numery kontaktowe i musi być certyfikat jakości - mus,