import time
from selenium import webdriver
from selenium import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(3)

# Switch context ot the frame, to work with frames
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("My text sent into the iFrame structure. I'm able to ")

# switch back to the default content:
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)



time.sleep(5)