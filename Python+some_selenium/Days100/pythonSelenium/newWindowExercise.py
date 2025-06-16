import time
from selenium import webdriver
from selenium import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
window_names = driver.window_handles #handles the whole window name in the list

# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()

driver.switch_to.window(window_names[1]) #switching the tabs, -> activates the given window in tabs
mail_to_mentor = driver.find_element(By.XPATH, "//div[@id='interview-material-container']/div/div/p[@class='im-para red']/strong").text
driver.close() #closes the current opened window

driver.switch_to.window(window_names[0])
driver.find_element(By.ID, "username").send_keys(mail_to_mentor)
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.ID, "terms").click()
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10) #Explicit wait
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

alert_text = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
assert alert_text == "Incorrect username/password."



time.sleep(5)