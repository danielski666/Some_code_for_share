from selenium.webdriver.common.by import By

from pageObjects.checkout_page import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()# XPATH version
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    mail = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.mail)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_check(self):
        return self.driver.find_element(*HomePage.check)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.successMessage)