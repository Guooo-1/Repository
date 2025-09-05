# from page.login_page import *
# import allure
#
# @allure.feature("登录功能")
# def test_login(login):
#     pass



import allure
import pytest

# # 添加一个 Allure 环境信息 (这会生成一个 environment.xml 文件)
# allure.environment(browser="Chrome", os="macOS")


@allure.feature("登录功能")
@allure.title("测试登录功能")
@allure.description("这是一个登录功能的测试用例")
def test_login(login):
    with allure.step("步骤 1: 开始登录测试"):
        print("✅ Allure step 1")

    with allure.step("步骤 2: 执行登录操作"):
        print("✅ Allure step 2")

    with allure.step("步骤 3: 验证登录结果"):
        assert True
        allure.attach("登录成功", name="结果", attachment_type=allure.attachment_type.TEXT)