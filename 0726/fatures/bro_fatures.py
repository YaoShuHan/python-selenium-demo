# -*- coding: utf-8 -*-

from selenium import webdriver

class myBrowser():
    driver = None

    def __init__(self,  url):
        self.driver = webdriver.Chrome()
        self.url = url

    @staticmethod
    def tobowser(url):
        if(myBrowser.driver == None):
            myBrowser.driver=webdriver.Chrome()
        myBrowser.driver.get(url)
        myBrowser.driver.maximize_window()

    @staticmethod
    def onlybrowser():
        if myBrowser.driver is None:
            myBrowser.driver = webdriver.Chrome()
        else:
            pass
