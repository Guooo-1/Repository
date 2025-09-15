from page.add_physical_charging_station_page import *
import allure

@allure.feature("新增物理场站")
def test_add_physical_station(add_physical_charging_station):
    browser = add_physical_charging_station
    #点击加号
    browser.click_add_button()
    #输入场站名称
    browser.input_physical_charging_station_name()
    #选择电价区域下拉框
    browser.select_electricity_area()
    #选择场站地域
    browser.select_physical_charging_station_area()
    #随机点击场站定位
    browser.random_click_map()
    #点击投运日期
    browser.select_launch_date()
    #确定按钮
    browser.click_sure_button()

