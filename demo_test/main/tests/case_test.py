# -*- coding: utf-8 -*-
import unittest
from tests.home.login_tests import LoginTests
from fatures.bro_fatures import myBrowser
from selenium import webdriver

baseUrl = "https://mail.qq.com"
# myBrowser(webdriver.Chrome(), baseUrl)

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(LoginTests("test_qqlogin"))
    unittest.main()
