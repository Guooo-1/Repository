from base.base_api import *
from ele_loctor.add_charging_station_loctor import *
from time import sleep

class add_charging_station(Base):
    def add_charging_station(self):             #点击加号
        self.click_eles(*add_button)
        sleep(1)

    def charging_station_name(self,text):
        self.input_texts(*charging_station_name,text)
        sleep(1)




    def sure_button(self):
        self.click_eles(*sure_button)
        sleep(1)