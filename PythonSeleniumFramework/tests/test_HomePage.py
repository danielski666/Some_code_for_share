import pytest

from TestData.HomePageData import HomePageData
from pageObjects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, getData):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        home_page.get_name().send_keys(getData["firstname"])
        home_page.get_email().send_keys(getData["lastname"])
        home_page.get_password().send_keys("0123456")
        home_page.get_check().click()
        self.selectOptionByText(home_page.get_gender(), getData["gender"])
        home_page.get_submitForm().click()

        alertText = home_page.get_success_message().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getData("TestCase2"))
    def getData(self, request):
        return request.param

