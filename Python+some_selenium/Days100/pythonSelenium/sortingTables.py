import time
from selenium import webdriver
from selenium import By


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(3)

# click on table header to sort all products
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# collect all product names -> store in vegeList
browserVeggie = driver.find_elements(By.XPATH, "//tr/td[1]")
browserVeggieListText = []
for veggie in browserVeggie:
    browserVeggieListText.append(veggie.text)

originalSortedList = browserVeggieListText.copy()
# apply sort to the list and create new one sorted -> newSortedList
browserVeggieListText.sort()
# assert that the lists are exactly the same :)
assert browserVeggieListText == originalSortedList
time.sleep(5)