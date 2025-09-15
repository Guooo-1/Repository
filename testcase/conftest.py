from selenium import webdriver
import pytest
from page.login_page import Login
from page.main_choose_page import main_choose
from page.add_physical_charging_station_page import add_physical_charging_station
from page.add_physical_charging_gun_page import add_physical_charging_gun
from page.add_physical_charging_rgv_page import add_physical_charging_rgv
from page.add_physical_charging_host_page import add_physical_charging_host
from page.add_charging_station_page import add_charging_station
from common.tools import *

#定义一个基础夹具，仅负责启动浏览器（供其他fixture依赖）
@pytest.fixture(name = 'browser_driver')
def browser_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver #传递driver给依赖他的fixture
    driver.quit() #测试结束后关闭浏览器

# 登录fixture依赖基础fixture，复用同一个driver
@pytest.fixture(name='login')
def login_fixture(browser_driver):
    driver = browser_driver
    url = 'http://internal.elu-energy.com:900/#/login'
    driver.get(url)
    browser = Login(driver)
    browser.input_user("郭馨文")
    browser.input_password("ELU123456")
    browser.click_login()
    return browser

# 登录智慧充电
@pytest.fixture(name='main_choose_smart_charging')
def main_choose_fixture(login, browser_driver):
    browser = main_choose(browser_driver)
    browser.choose_module_smart_charging()
    return browser

# 登录综合管理后台
@pytest.fixture(name='main_choose_integrated_management')
def main_choose_integrated_management(login, browser_driver):
    browser = main_choose(browser_driver)
    browser.choose_module_integrated_management()
    yield browser

#新增物理场站
@pytest.fixture(name = 'add_physical_charging_station')
def add_physical_physical_station(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_station(browser_driver)
    return browser


#新增物理充电主机
@pytest.fixture(name = 'add_physical_charging_host')
def add_physical_charging_host_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_host(browser_driver)
    return browser


#新增物理充电枪
@pytest.fixture(name = 'add_physical_charging_gun')
def add_physical_charging_gun_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_gun(browser_driver)
    return browser


# 新增物理RGV
@pytest.fixture(name = 'add_physical_charging_rgv')
def add_physical_charging_rgv_fixture(main_choose_integrated_management,browser_driver):
    browser = add_physical_charging_rgv(browser_driver)
    return browser


@pytest.fixture(name = 'add_charging_station')
def add_charging_station_fixture(main_choose_smart_charging,browser_driver):
    browser = add_charging_station(browser_driver)
    return browser




