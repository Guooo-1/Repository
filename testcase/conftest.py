import configparser

from selenium import webdriver
from time import sleep
import pytest
from page.login_page import Login
from page.main_choose_page import main_choose
from page.add_charging_station_page import add_charging_station
from page.add_physical_charging_station_page import add_physical_charging_station
from page.add_physical_charging_gun_page import add_physical_charging_gun
from page.add_physical_charging_rgv_page import add_physical_charging_rgv
from page.add_physical_charging_host_page import add_physical_charging_host
from common.tools import *

#定义一个基础夹具，仅负责启动浏览器（供其他fixture依赖）
@pytest.fixture(name = 'browser_driver')
def browser_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver #传递driver给依赖他的fixture
    driver.quit() #测试结束后关闭浏览器

#数据库连接步骤
@pytest.fixture(name = 'db')
def connect_db(request):
    db_config={
        'host': 'localhost',
        'user':'root',
        'password':'Aa123456!',
        'database':'user'
    }
    db_connection = DB(**db_config)
    db_connection.connect()
    yield db_connection
    db_connection.close()


#login_user
@pytest.fixture(name = 'login_db')
def login_db(db):
    try:
        #查询用户信息
        user_id = 1 #要是换的话记得修改
        sql = "select name,password from login_user_T where user_id = %s"      #这个地方的占位符不要加引号，比如‘%s’这样不对，数据库中user_id为int类型，加完双引号为字符串，肯定找不到匹配的。
        user_info = db.Search_One(sql,(user_id,))
        if not user_info:
            pytest.fail(f"未找到 user_id={user_id} 的用户")
        username = user_info['name']            #我连接数据库时让他返回的是字典的形式，这个地方直接用字典取值就行，不要转成列表。
        password = user_info['password']
        print(f"从数据库中获取登录信息：用户名 = '{username}', 密码='{password}'")
        yield (username, password)

    except Exception as e:
        print("查询用户信息失败")
        raise


#登录fixture依赖基础fixture，复用同一个driver
@pytest.fixture(name = 'login')
def login_fixture(browser_driver, login_db):
    driver = browser_driver
    url = 'http://internal.elu-energy.com:900/#/login'
    driver.get(url)
    browser = Login(driver)
    #输入用户名
    browser.input_user(login_db[0])
    #输入密码
    browser.input_password(login_db[1])
    #点击登录
    browser.click_login()
    yield browser   #登录后把browser传递给测试用例


#主页选择fixture依赖登录fixture，复用同一个driver
#登录智慧充电
@pytest.fixture(name ='main_choose_smart_charging')
def main_choose_fixture(login, browser_driver):
    browser = main_choose(browser_driver)
    browser.choose_module_smart_charging()
    yield browser   #选择主页后把browser传递给测试用例

#登录综合管理后台
@pytest.fixture(name = 'main_choose_integrated_management')
def main_choose_integrated_management(login, browser_driver):
    browser = main_choose(browser_driver)
    browser.choose_module_integrated_management()
    yield browser


#新增逻辑场站
@pytest.fixture(name = 'add_charging_station')
def add_charging_station_fixture(login, main_choose_smart_charging,browser_driver):
    browser = add_charging_station(browser_driver)
    browser.add_charging_station()
    #输入场站名称
    browser.charging_station_name("测试001")
    browser.sure_button()
    yield browser


#新增物理场站
@pytest.fixture(name = 'add_physical_charging_station')
def add_physical_physical_station(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_station(browser_driver)
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

#新增充电主机
@pytest.fixture(name = 'add_physical_charging_host')
def add_physical_charging_host_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_gun(browser_driver)
    #点击外层设备管理
    browser.click_equipment_management()
    #点击内层设备管理
    browser.click_equipment_management_inner()
    #点击加号
    browser.click_add_button()
    #点击单个新增
    browser.click_single_add_button()
    #点击所属产品
    browser.click_associated_product()
    #选择所属产品
    browser.choose_associated_product()
    #输入主机名称
    browser.input_device_name()
    #点击随机生成
    browser.click_random_creat()
    #点击设备分类
    browser.click_device_type()
    #选择设备
    browser.choose_device_type()
    #点击关联场站
    browser.click_related_station()
    #选择关联场站
    browser.choose_related_station()
    #点击确定按钮
    browser.click_sure_button()

#新增物理充电枪
@pytest.fixture(name = 'add_physical_charging_gun')
def add_physical_charging_gun_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_gun(browser_driver)
    #点击外层设备管理
    browser.click_equipment_management()
    #点击内层设备管理
    browser.click_equipment_management_inner()
    #点击加号
    browser.click_add_button()
    #点击单个新增
    browser.click_single_add_button()
    #点击所属产品
    browser.click_associated_product()
    #选择所属产品
    browser.choose_associated_product()
    #输入主机名称
    browser.input_device_name()
    #点击随机生成
    browser.click_random_creat()
    #点击设备分类
    browser.click_device_type()
    #选择设备
    browser.choose_device_type()
    #点击关联场站
    browser.click_related_station()
    #选择关联场站
    browser.choose_related_station()
    #点击确定按钮
    browser.click_sure_button()

    # 新增物理RGV
@pytest.fixture(name = 'add_physical_charging_rgv')
def add_physical_charging_rgv_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_rgv(browser_driver)
    #点击外层设备管理
    browser.click_equipment_management()
    #点击内层设备管理
    browser.click_equipment_management_inner()
    #点击加号
    browser.click_add_button()
    #点击单个新增
    browser.click_single_add_button()
    #点击所属产品
    browser.click_associated_product()
    #选择所属产品
    browser.choose_associated_product()
    #输入主机名称
    browser.input_device_name()
    #点击随机生成
    browser.click_random_creat()
    #点击设备分类
    browser.click_device_type()
    #选择设备
    browser.choose_device_type()
    #点击关联场站
    browser.click_related_station()
    #选择关联场站
    browser.choose_related_station()
    #点击确定按钮
    browser.click_sure_button()

