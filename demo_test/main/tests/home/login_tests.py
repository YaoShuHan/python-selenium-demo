# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.page_fatures import *
from fatures.bro_fatures import myBrowser
import unittest

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = myBrowser.tobowser("https://mail.qq.com")
        # 访问mail.qq
        # baseUrl = "https://mail.qq.com"
        # self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        # self.driver.get(baseUrl)

    def test_qqlogin(self):
        LoginPage(self.driver)

    def tearDown(self):
        # 验证登陆成功
        try:
            wri_let = self.driver.find_element(By.ID, "composebtn")
            if wri_let is not None:
                print("登陆成功！")
                self.driver.quit()
        except:
                print("登陆失败！")
                self.driver.quit()

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(LoginTests("test_validlogin"))
    unittest.main()
