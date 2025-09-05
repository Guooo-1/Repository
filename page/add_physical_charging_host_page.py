from base.base_api import *
import allure
from ele_loctor.add_physical_charging_host_loctor import *
from time import sleep
class add_physical_charging_host(Base):
    @allure.step('点击外层设备管理')
    def click_equipment_management(self):
        self.click_ele(*equipment_management)
        sleep(1)
    @allure.step('点击内层设备管理')
    def click_equipment_management_inner(self):
        self.click_eles(*equipment_management_inner)
        sleep(1)
    @allure.step('点击加号按钮')
    def click_add_button(self):
        self.click_eles(*add_button)
        sleep(2)