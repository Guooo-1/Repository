from selenium import webdriver
from time import sleep
import pytest
from page.login_page import Login
from page.main_choose_page import main_choose
from page.add_charging_station_page import add_charging_station

# @pytest.fixture(name='login')
# def Login_fixture():
#     url = 'http://internal.elu-energy.com:900/#/login'
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.maximize_window()
#     driver.implicitly_wait(5)  #隐式等待，让浏览器驱动（driver）在查找网页元素时，若元素未立即找到，会自动等待最多 5 秒；# 若 5 秒内元素出现则继续执行，超时仍未出现才报错。
#     browser = Login(driver)
#     #开始操作
#     #输入用户名
#     browser.input_user("郭馨文")
#     #输入密码
#     browser.input_password("ELU123456")
#     #点击登录
#     browser.click_login()


# @pytest.fixture(name='main_chooce')
# def main_chooce_fixture():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(5)
#     browser = main_choose(driver)
#     #开始操作
#     browser.choose_module()


#定义一个基础夹具，仅负责启动浏览器（供其他fixture依赖）
@pytest.fixture(name = 'browser_driver')
def browser_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver #传递driver给依赖他的fixture
    driver.quit() #测试结束后关闭浏览器


#登录fixture依赖基础fixture，复用同一个driver
@pytest.fixture(name = 'login')
def login_fixture(browser_driver):
    driver = browser_driver
    url = 'http://internal.elu-energy.com:900/#/login'
    driver.get(url)
    browser = Login(driver)
    #开始操作
    #输入用户名
    browser.input_user("郭馨文")
    #输入密码
    browser.input_password("ELU123456")
    #点击登录
    browser.click_login()
    yield browser   #登录后把browser传递给测试用例


#主页选择fixture依赖登录fixture，复用同一个driver
@pytest.fixture(name ='main_chooce')
def main_chooce_fixture(login, browser_driver):
    browser = main_choose(browser_driver)
    browser.choose_module()
    yield browser   #选择主页后把browser传递给测试用例

@pytest.fixture(name = 'add_charging_station')
def add_charging_station_fixture(login, main_chooce,browser_driver):
    browser = add_charging_station(browser_driver)
    browser.add_charging_station()
    #输入场站名称
    browser.charging_station_name("测试001")
    browser.sure_button()
    yield browser