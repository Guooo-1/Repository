from base.base_api import *
import allure
from ele_loctor.add_physical_charging_host_loctor import *
from time import sleep
from datetime import datetime
class add_physical_charging_rgv(Base):
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
    @allure.step('点击单个新增')
    def click_single_add_button(self):
        self.click_eles(*single_add_button)
        sleep(2)
    @allure.step('点击所属产品')
    def click_associated_product(self):
        self.click_eles(*associated_product)
        sleep(1)
    @allure.step('选择所属产品-rgv')
    def choose_associated_product(self):
        self.click_eles(*associated_product)
        #显示等待
        wait = WebDriverWait(self.driver, 10)
        charging_rgv_xpath = "(//li[contains(@class, 'el-select-dropdown__item') and .//span[contains(normalize-space(text()), '中能坤域第一代RGV')]])[2]"
        try:
            # 等待选项出现在 DOM 中
            option_ele = wait.until(EC.presence_of_element_located((By.XPATH, charging_rgv_xpath)))
            # 滚动到视野中央，使用JavaScript命令滚动页面，使目标元素位于视窗中央。之后调用sleep(0.3)暂停程序0.3秒，以确保滚动操作已完成。
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_ele)
            sleep(1)  # 等待滚动完成
            # 使用 JS 点击（规避不可交互问题），通过JavaScript直接对option_ele执行点击操作，目的是解决某些情况下元素不可交互的问题。然后再次暂停程序0.5秒，以确保点击事件已被处理。
            self.driver.execute_script("arguments[0].click();", option_ele)
            sleep(0.8)
        except Exception as e:
            self.driver.save_screenshot("fail_select_liaoning.png")
            raise e

    @allure.step('输入设备名称')
    def input_device_name(self):
        date_str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.input_texts(*device_name, f'{date_str}-RGV')
        sleep(1)

    @allure.step('输入设备SN码')
    def click_random_creat(self):
        self.click_ele(*click_random_create)
        sleep(1)

    @allure.step('点击设备分类')
    def click_device_type(self):
        self.click_eles(*device_type)
        sleep(1)

    @allure.step('选择设备分类-充电桩/RGV/机械臂')
    def choose_device_type(self):
        wait = WebDriverWait(self.driver, 10)
        device_type_xpath = "(//li[contains(@class, 'el-select-dropdown__item') and .//span[contains(normalize-space(text()), '充电桩/RGV/机械臂')]])[2]"
        try:
            # 等待选项出现在 DOM 中
            option_ele = wait.until(EC.presence_of_element_located((By.XPATH, device_type_xpath)))
            # 滚动到视野中央，使用JavaScript命令滚动页面，使目标元素位于视窗中央。之后调用sleep(0.3)暂停程序0.3秒，以确保滚动操作已完成。
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_ele)
            sleep(1)  # 等待滚动完成
            # 使用 JS 点击（规避不可交互问题），通过JavaScript直接对option_ele执行点击操作，目的是解决某些情况下元素不可交互的问题。然后再次暂停程序0.5秒，以确保点击事件已被处理。
            self.driver.execute_script("arguments[0].click();", option_ele)
            sleep(1)
        except Exception as e:
            self.driver.save_screenshot("fail_select_liaoning.png")
            raise e
    @allure.step('点击关联场站')
    def click_related_station(self):
        self.click_eles(*related_station)
        sleep(1)

    @allure.step('选择关联场站')
    def choose_related_station(self):
        wait = WebDriverWait(self.driver, 10)
        related_station_xpath = "(//li[contains(@class, 'el-select-dropdown__item') and .//span[contains(normalize-space(text()), 'test-auto-2025-09-04_17:18:11')]])[2]"
        try:
            # 等待选项出现在 DOM 中
            option_ele = wait.until(EC.presence_of_element_located((By.XPATH, related_station_xpath)))
            # 滚动到视野中央，使用JavaScript命令滚动页面，使目标元素位于视窗中央。之后调用sleep(0.3)暂停程序0.3秒，以确保滚动操作已完成。
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_ele)
            sleep(1)  # 等待滚动完成
            # 使用 JS 点击（规避不可交互问题），通过JavaScript直接对option_ele执行点击操作，目的是解决某些情况下元素不可交互的问题。然后再次暂停程序0.5秒，以确保点击事件已被处理。
            self.driver.execute_script("arguments[0].click();", option_ele)
            sleep(1)
        except Exception as e:
            self.driver.save_screenshot("fail_select_liaoning.png")
            raise e

    @allure.step('点击确定按钮')
    def click_sure_button(self):
        self.click_eles(*sure_button)
        sleep(1)
