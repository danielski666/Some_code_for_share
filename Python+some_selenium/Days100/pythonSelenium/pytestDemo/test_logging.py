import logging
import pytest


@pytest.LogCaptureFixture
def test_logging_demo():
    logger = logging.getLogger(__name__) # pass __name__ to log the tesst case name

    fileHandler = logging.FileHandler("logfile.log")
    loggingFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(loggingFormat)

    logger.addHandler(fileHandler)  # need to be passed filehandler object

    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed.")
    logger.info("Information statement.")
    logger.warning("Something is in warning mode.")
    logger.error("A major error has happend!")
    logger.critical("Critical Issue!")