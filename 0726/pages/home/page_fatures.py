# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from ele_dic import points

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        # 开始登陆
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame("login_frame")

        """直接点击头像登陆"""
        qqimage = findElements(self.driver, 'qqlog')
        qqimage.click()

        # """直接点击头像登陆"""
        # qqimage = self.driver.find_element(By.ID, "img_out_641143880")
        # qqimage.click()

        """输入账号密码登陆"""
        # switch_log = driver.find_element(By.ID, "switcher_plogin")
        # switch_log.click()
        # qqname = driver.find_element(By.ID, "u")
        # qqname.send_keys("641143880")
        # qqpassword = driver.find_element(By.ID, "p")
        # qqpassword.send_keys("a89331787")
        # log_btn = driver.find_element(By.ID, "login_button")
        # log_btn.click()

def findElements(driver, name):
    try:
        ele = points[name]
        type = ele['type']
        locator = ele['locator']
        if type == 'id':
            return driver.find_element_by_id(locator)
        else:
            return -1

    except Exception, e:
        print Exception, ":", e, "寻找元素失败"
        return -1