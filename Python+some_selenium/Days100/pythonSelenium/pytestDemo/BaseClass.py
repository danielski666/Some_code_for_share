import inspect
import logging


class BaseClass:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)  # pass __name__ to log the test case name

        file_handler = logging.FileHandler("../../logfile.log")
        logging_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(logging_format)

        logger.addHandler(file_handler)  # need to be passed filehandler object
        logger.setLevel(logging.INFO)
        return logger