"""
这里用来写一些维护driver的方法，例如send.keys,click,find_elements
"""
from selenium.webdriver.common.by import By         #引入 Selenium 定位网页元素的 “定位策略常量”
from selenium.webdriver.support.ui import WebDriverWait     #显示等待
from selenium.webdriver.support import expected_conditions as EC    #引入 “预设等待条件集合” 并简写为 EC，配合显示等待使用
from traceback import print_exc     #print_exc 函数会讲当前异常信息输出到标准错误到控制台上


class Base:
    def __init__(self,driver):
        self.driver = driver
        #选择元素的字典
        self.loctor = {
            "id":By.ID,
            "name":By.NAME,
            "class name":By.CLASS_NAME,
            "xpath":By.XPATH,
            "tag name":By.TAG_NAME,
            "css":By.CSS_SELECTOR,
            "link text":By.LINK_TEXT,
            "partial link text":By.PARTIAL_LINK_TEXT
        }


    #封装一个查找一个元素的方法
    def find_element(self,loc_method,loc):
        """
        :param loc_method:传入要操作的定位方式：xpath,id,name...
        :param loc: 具体元素的值
        :return:
        """
        try:
            return WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located((self.loctor[loc_method],loc)))
        except Exception as e:
            raise Exception(f"查找元素失败：定位方式={loc_method}，定位值={loc}，错误：{str(e)}")


    #封装一个查找一组元素的方法
    def find_elements(self,loc_method,loc,num):
        """
        :param loc_method: 传入要操作的定位方式
        :param loc: 具体元素的值
        :param num: 要操作第几个
        :return:
        """
        try:
            return WebDriverWait(self.driver,10,0.5).until(
                EC.presence_of_all_elements_located((self.loctor[loc_method],loc)))[num]
        except Exception as e:
            #return "元素超时，没有找到"
            raise Exception(f"查找元素失败，定位方式：{loc_method}，定位值：{loc}，索引：{num}，错误信息：{str(e)}")


    #点击一个元素
    def click_ele(self,loc_method,loc):
        self.find_element(loc_method,loc).click()


    #点击一组元素
    def click_eles(self,loc_method,loc,num):
        self.find_elements(loc_method,loc,num).click()


    #输入一个内容
    def input_text(self,loc_method,loc,text):
        ele = self.find_element(loc_method,loc)
        #先清空
        ele.clear()
        #在输入
        ele.send_keys(text)


    #输入一组内容
    def input_texts(self,loc_method,loc,num,text):
        eles = self.find_elements(loc_method,loc,num)
        #先清空
        eles.clear()
        #再输入
        eles.send_keys(text)


    #句柄切换
    def win_(self,num):
        win = self.driver.window_handles
        self.driver.switch_to.window(win[num])


    #返回文本内容
    def get_content(self,loc_method,loc):
        text = self.find_element(loc_method,loc).text
        return text