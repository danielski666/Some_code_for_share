import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects import home_page


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresensce(self, text):
        wait = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
        return wait

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)  # pass __name__ to log the test case name

        file_handler = logging.FileHandler("logfile.log")
        logging_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(logging_format)

        logger.addHandler(file_handler)  # need to be passed filehandler object
        logger.setLevel(logging.DEBUG)
        return logger