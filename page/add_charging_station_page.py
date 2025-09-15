import allure
from time import sleep
from ele_loctor.add_charging_station_locter import *
import random
from datetime import datetime
from base.base_api import *
from pathlib import Path

class add_charging_station(Base):
    @allure.step("点击加号")
    def click_add_button_charging_station(self):
        self.click_eles(*add_button)
        sleep(1)

    @allure.step("关联场站")
    def relation_charging_station(self):
        self.click_eles(*relation_station)
        sleep(1)
        self.click_eles(*select_drop_down_box)
        sleep(1)
    @allure.step("输入充电站名称")
    def input_charging_station(self):
        random_num = random.randint(1, 99)
        date_str = datetime.now().strftime("%Y-%m-%d_%H")
        related_station_name = "test_auto" + date_str + "_" + str(random_num) + "_充电站"
        self.input_texts(*charging_station_name,related_station_name)
        sleep(1)
    @allure.step("选择充电站类型")
    def select_charging_station_type(self):
        self.click_eles(*click_charging_station_type)
        # 显式等待：等待“辽宁”选项出现（无论是否可见，先确保在 DOM 中）
        wait = WebDriverWait(self.driver, 10)
        # 更精准的选项定位：兼容 span 文本、li 结构
        liaoning_xpath = "(//li[contains(@class, 'el-select-dropdown__item') and .//span[contains(normalize-space(text()), '公共')]])"
        try:
            # 等待选项出现在 DOM 中
            option_ele = wait.until(EC.presence_of_element_located((By.XPATH, liaoning_xpath)))
            # 滚动到视野中央，使用JavaScript命令滚动页面，使目标元素位于视窗中央。之后调用sleep(0.3)暂停程序0.3秒，以确保滚动操作已完成。
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option_ele)
            sleep(0.3)  # 等待滚动完成
            # 使用 JS 点击（规避不可交互问题），通过JavaScript直接对option_ele执行点击操作，目的是解决某些情况下元素不可交互的问题。然后再次暂停程序0.5秒，以确保点击事件已被处理。
            self.driver.execute_script("arguments[0].click();", option_ele)
            sleep(0.5)
        except Exception as e:
            self.driver.save_screenshot("fail_select_liaoning.png")
            raise e

    @allure.step("选择营业时间")
    def select_launch_date(self):
        # 点击投运日期边框
        self.click_eles(*select_start_business_hours)
        sleep(1)
        self.click_eles(*click_time_button)
        sleep(1)

    @allure.step("选择充电站标签")
    def select_charging_station_tag(self):
        self.click_eles(*click_charging_station_label)
        sleep(1)
        self.click_ele(*select_charging_Station_label)
        sleep(1)

    @allure.step("点击充电站图片")
    def click_charging_station_image(self):
        #上传图片的框
        # picture = self.click_eles(*click_charging_station_image)
        #上传图片，获取当权工作目录
        current_path = Path.cwd()
        img1 = current_path / "image" / "GG-bond.jpg"
        self.input_texts(*click_charging_station_image,img1)
        sleep(1)
