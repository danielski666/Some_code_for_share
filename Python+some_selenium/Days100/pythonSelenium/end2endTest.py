import time
from selenium import webdriver
from selenium import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
# driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()# XPATH version
cards_on_site = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for card in cards_on_site:
    product_name = card.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        card.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

driver.close()



time.sleep(5)