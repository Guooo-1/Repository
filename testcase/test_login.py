from page.login_page import *
import allure

@allure.feature("登录功能")
def test_login(login):
    browser = login