import allure

@allure.feature("新增物理充电枪")
def test_add_physical_rgv(add_physical_charging_rgv):
    browser = add_physical_charging_rgv
    # 点击外层设备管理
    browser.click_equipment_management()
    # 点击内层设备管理
    browser.click_equipment_management_inner()
    # 点击加号
    browser.click_add_button()
    # 点击单个新增
    browser.click_single_add_button()
    # 点击所属产品
    browser.click_associated_product()
    # 选择所属产品
    browser.choose_associated_product()
    # 输入主机名称
    browser.input_device_name()
    # 点击随机生成
    browser.click_random_creat()
    # 点击设备分类
    browser.click_device_type()
    # 选择设备
    browser.choose_device_type()
    # 点击关联场站
    browser.click_related_station()
    # 选择关联场站
    browser.choose_related_station()
    # 点击确定按钮
    browser.click_sure_button()
