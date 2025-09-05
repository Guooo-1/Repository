from base.base_api import *
import allure
from ele_loctor.add_physical_charging_station_loctor import *
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
from datetime import datetime

class add_physical_charging_station(Base):


    @allure.step("点击添加按钮")
    def click_add_button(self):
        self.click_eles(*click_add_button)


    @allure.step("请输入物理场站名称")
    def input_physical_charging_station_name(self):
        #获取当前日期和时间
        date_str = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.input_texts(*physical_station_name,f'test-auto-{date_str}')
        sleep(1)


    @allure.step("选择电价区域")
    def select_electricity_area(self):
        # 点击下拉框触发器
        self.click_eles(*electricity_area)
        # 显式等待：等待“辽宁”选项出现（无论是否可见，先确保在 DOM 中）
        wait = WebDriverWait(self.driver, 10)
        # 更精准的选项定位：兼容 span 文本、li 结构
        liaoning_xpath = "(//li[contains(@class, 'el-select-dropdown__item') and .//span[contains(normalize-space(text()), '辽宁')]])[2]"
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


    @allure.step("选择场站地域")
    def select_physical_charging_station_area(self):
        self.click_eles(*physical_station_area)
        #等待级联选择器加载完成
        wait = WebDriverWait(self.driver, 10)

        #点击省份
        first_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='el-cascader-panel']//li[.//span[text()='辽宁省']]")))
        first_menu.click()
        sleep(0.5)

        #点击城市
        second_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='el-scrollbar el-cascader-menu'][2]//li[.//span[text()='沈阳市']]")))
        second_menu.click()
        sleep(0.5)

        #点击区县
        third_menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='el-scrollbar el-cascader-menu'][3]//li[.//span[text()='沈北新区']]")))
        third_menu.click()
        sleep(0.5)

    @allure.step("随机点击地图")
    def random_click_map(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            # Step 1: 等待地图容器（外层 div）
            map_container = wait.until(
                EC.presence_of_element_located((By.ID, "map-coordinates"))
            )
            print("✅ 找到地图容器")

            # Step 2: 滚动到地图位置，确保可见
            self.driver.execute_script("arguments[0].scrollIntoView(true);", map_container)
            sleep(1)  # 等待滚动完成

            # Step 3: 等待内部的 <canvas> 元素（真正可交互的部分）
            canvas = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#map-coordinates canvas"))
            )
            print("✅ 找到地图 canvas 元素")

            # Step 4: 获取地图容器的位置和尺寸
            location = map_container.location
            size = map_container.size
            width = size['width']
            height = size['height']

            # Step 5: 在地图区域内生成随机偏移量（避免边缘）
            offset_x = random.randint(10, width - 10)
            offset_y = random.randint(10, height - 10)

            # Step 6: 计算页面绝对坐标（clientX, clientY 使用）
            absolute_x = location['x'] + offset_x
            absolute_y = location['y'] + offset_y

            print(f"🖱️  将在坐标 ({absolute_x}, {absolute_y}) 模拟点击")

            # ✅ Step 7: 触发 mousedown 事件
            self.driver.execute_script("""
                    var target = arguments[0];
                    var event = new MouseEvent('mousedown', {
                        view: window,
                        bubbles: true,          // 事件冒泡
                        cancelable: true,       // 可被阻止
                        clientX: arguments[1],  // 鼠标 X 坐标（页面级）
                        clientY: arguments[2],  // 鼠标 Y 坐标
                        button: 0,              // 左键点击
                        buttons: 1              // 当前按下的按钮：1=左键
                    });
                    target.dispatchEvent(event);
                """, canvas, absolute_x, absolute_y)

            print("✅ 触发 mousedown 事件")

            # ✅ Step 8: 模拟鼠标抬起（mouseup）
            # 等待 100-300ms，模拟人类操作延迟
            sleep(0.2)

            self.driver.execute_script("""
                    var target = arguments[0];
                    var event = new MouseEvent('mouseup', {
                        view: window,
                        bubbles: true,
                        cancelable: true,
                        clientX: arguments[1],
                        clientY: arguments[2],
                        button: 0,
                        buttons: 0              // 抬起后无按钮按下
                    });
                    target.dispatchEvent(event);
                """, canvas, absolute_x, absolute_y)

            print("✅ 触发 mouseup 事件")
            print(f"🎉 已成功随机点击地图上的位置：({absolute_x}, {absolute_y})")

            # 可选：等待地图响应（如弹出信息窗）
            sleep(1)

        except Exception as e:
            print(f"点击地图失败：{e}")
            raise  # 保留异常堆栈，便于调试


    @allure.step('选择投运日期')
    def select_launch_date(self):
        #点击投运日期边框
        self.click_eles(*launch_date)
        sleep(1)
        try:
            wait = WebDriverWait(self.driver, 10)
            #定位日期表格中的2号
            date_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//td[@class = 'available']/div/span[text() = 2]/ancestor::td")))
            date_element.click()
            print("✅ 选择日期成功")
        except Exception as e:
            print(f"选择日期失败：{e}")
        sleep(1)


    @allure.step("点击确定按钮")
    def click_sure_button(self):
        """点击确定按钮保存场站"""
        try:
            self.click_eles(*click_sure_button)
            sleep(1)
            print("已点击确定按钮")
        except Exception as e:
            print(f"点击确定按钮失败: {e}")

























