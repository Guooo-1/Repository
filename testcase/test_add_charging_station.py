import allure

@allure.feature("新增场站")
def test_add_charging_station(add_charging_station):
    browser = add_charging_station
    #点击加号
    browser.click_add_button_charging_station()
    #点击关联场站
    browser.relation_charging_station()
    #输入充电站名称
    browser.input_charging_station()
    #选择充电站类型
    browser.select_charging_station_type()
    browser.select_launch_date()
    #选择充电站标签
    browser.select_charging_station_tag()
    #点击充电站图片
    browser.click_charging_station_image()
