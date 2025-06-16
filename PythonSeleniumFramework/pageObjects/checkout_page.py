from selenium.webdriver.common.by import By

from pageObjects.confirm_page import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    btnPrimary = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    btnSuccess = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def get_card_footer(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def get_button_primary(self):
        return self.driver.find_element(*CheckOutPage.btnPrimary)

    def get_button_success(self):
        self.driver.find_element(*CheckOutPage.btnSuccess).click()
        return ConfirmPage(self.driver)
