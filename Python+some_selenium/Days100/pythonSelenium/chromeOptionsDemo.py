import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import By


# Not working... ToDo: later on find out what is wrong, e.g.: check again browser version, invoking, downloaded webdriver version, etc.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
cService = Service(executable_path="C:\\Users\\dispolatov\\PycharmProjects\\100Days\\drivers\\chromedriver-win64")
serv = webdriver.ChromeService(executable_path="drivers/chromedriver-win64")
driver = webdriver.Chrome(options="chrome_options", service=cService)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)




time.sleep(5)