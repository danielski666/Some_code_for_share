import time


from selenium import webdriver
from selenium import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5) #max time out for waiting for the elements, if the allement appear then time will be reduced


driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
driver.find_element(By.CSS_SELECTOR, "button[class='search-button]" and "button[type='submit']").click()
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
print(count)
assert count > 0
product_names, product_names_assertion = [], ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
for product in products:
    product.find_element(By.XPATH, "div/button").click()
    product_names.append(product.find_element(By.CLASS_NAME, "product-name").text)

for product_name in product_names:
    assert product_name in product_names_assertion
#go to the cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#time.sleep(5)
#apply promocode and proceed
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
#time.sleep(5)
wait = WebDriverWait(driver, 10) #Explicit wait
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
#Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum += int(price.text)
print(sum)
assert sum == 388
totalAmount = float(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == totalAmount
after_discount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert totalAmount > after_discount
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)








time.sleep(5)