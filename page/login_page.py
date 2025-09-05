from base.base_api import *
import allure
from ele_loctor.login_loctor import *
from time import sleep
from common.tools import *


class Login(Base):
    @allure.step("请输入用户名：{text}")
    def input_user(self,text):
        self.input_texts(*user,text)
        sleep(1)

    @allure.step("请输入密码，{text}")
    def input_password(self,text):
        self.input_texts(*password,text)
        sleep(1)
    @allure.step("点击登录")
    def click_login(self):
        self.click_ele(*login)
        sleep(2)