# coding=utf-8
'''
#——单元测试unittest基本概念

#——调用单元测试unittert函数
import unittest
#——引用selenium，获得驱动
from selenium import webdriver
#——强制休眠时间
import time

#——建立lei方法
class Test_baidu(unittest.TestCase):  #——必须引用（unittest.TestCase）
    #）——建立self实例（引用函数）
    def setUp(self): #——引用setUp作为预处理
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)

    #—方法二不引用setUp，进行获得驱动
    # def test_bai(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://www.baidu.com')
    #     time.sleep(2)
    #     self.driver.maximize_window()
    #     return self.driver
    # def test_baidu(self):
    #     driver = self.test_bai()
    #     time.sleep(3)
    #——单元测试用例一，每作为一个用例都可以建立新的测试用例实例（必须用test为首命名，否则测试不生效）
    def test_case01(self):
        self.driver.find_element_by_id('kw').send_keys('中国')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def test_case02(self):
        self.driver.find_element_by_link_text('新闻').click()
        time.sleep(3)
    #——使用tearDown作为预清理，系统自带
    def tearDown(self):
        self.driver.quit()
        time.sleep(3)
'''

from selenium import webdriver
import unittest
import time
from Ui_selenium.wangyi_email_.WY_class_fenghzhuang import baidu
from Ui_selenium.YMW_fengzhuang.ymw_class import ymw_bage

class Test_163mail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.close()
        #——初始化调用驱动
        self.t = baidu(self.driver)
        self.s = ymw_bage(self.driver)
        #——调用自定义参数使用，根据前面封装来使用
        # self.t = baidu()
        #self.s = ymw_bage()
    def test_WY(self):
        self.t.baidu_find()
        time.sleep(2)
        self.t.mail_login()
        time.sleep(2)
        self.t.email_write()
    def test_ymw(self):
        #——打开自定义参数调用是打开
        # self.s.ymw_open()
        # time.sleep(2)
        self.s.ymw_login()
        time.sleep(2)
        self.s.ymw_seacher()
        time.sleep(2)
    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    #——第二种测试方法



