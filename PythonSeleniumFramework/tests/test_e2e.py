import time


# @pytest.mark.usefixtures("setup") -> inherit from the BaseClass of the tests_
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.get_logger()

        self.driver.implicitly_wait(4)
        home_page = HomePage(self.driver)
        check_out_page = home_page.shop_items()
        log.info("get all card titles")
        cards_on_site = check_out_page.get_card_title()
        i = -1
        for card in cards_on_site:
            i += 1
            cardText = card.text
            log.info(cardText)

            #product_name = card.find_element(By.XPATH, "div/h4/a").text
            if cardText == "Blackberry":
                check_out_page.get_card_footer().click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        check_out_page.get_button_primary().click()
        #self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirm_page = check_out_page.get_button_success()
        log.info("Entering country name as ind")

        #self.driver.find_element(By.ID, "country").send_keys("ind")
        confirm_page.get_country_input().send_keys("ind")
        # moved to the BaseClass -> wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresensce("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirm_page.get_input_chosen_country().click()
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_page.get_checkbox().click()
        #self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        confirm_page.get_submit_button().click()
        #success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        success_text = confirm_page.get_alert_success().text
        log.info("text received from app is " + success_text)
        assert "Success! Thank asdyou!" in success_text

        time.sleep(5)


