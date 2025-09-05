from base.base_api import *
import allure
from ele_loctor.main_choose_loctor import *
from time import sleep


class main_choose(Base):
    def choose_module_smart_charging(self):
        self.click_eles(*smart_charging)
        sleep(1)

    def choose_module_integrated_management(self):
        self.click_eles(*integrated_management_backend)
        sleep(1)