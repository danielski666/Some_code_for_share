from pytestDemo.BaseClass import BaseClass
import pytest



@pytest.mark.usefixtures("setup", "data_load")
class TestExample2(BaseClass):

    def test_edit_profile(self, data_load):
        log = self.get_logger()
        log.info(data_load[0])
        #print(data_load[0])
        log.info(data_load[2])
        #print(data_load[2])