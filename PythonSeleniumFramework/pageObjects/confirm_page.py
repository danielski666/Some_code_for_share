from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver


    country_input = (By.ID, "country")
    input_chosen_country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    btn_submit = (By.CSS_SELECTOR, "input[type='submit']")
    allert_success = (By.CLASS_NAME, "alert-success")


    def get_country_input(self):
        return self.driver.find_element(*ConfirmPage.country_input)

    def get_input_chosen_country(self):
        return self.driver.find_element(*ConfirmPage.input_chosen_country)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.country_input)

    def get_submit_button(self):
        return self.driver.find_element(*ConfirmPage.btn_submit)

    def get_alert_success(self):
        return self.driver.find_element(*ConfirmPage.allert_success)