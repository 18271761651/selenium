# -*- coding:utf-8 -*-
# user:Liukang
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.common.base_page import BasePage

class LoginPage(BasePage):
    url="http://shop.hlwulian.com"
    username = (By.NAME, "username")    # 用户名
    password = (By.NAME, "password")    # 密码
    loginButton = (By.XPATH, '//*[@id="app"]/div/div[2]/form/button')   # 登录按钮
    home_url = 'http://shop.hlwulian.com/#/dashboard'   #首页网址

    # 元素的操作流程
    def login(self,username='lleg',password='123456'):
        # 访问URL
        self.open(self.url)
        # 输入用户名
        self.input(self.username,username)
        # 输入密码
        self.input(self.password,password)
        # 点击登录按钮
        self.click(self.loginButton)
        self.url_to_be(self.home_url)

if __name__=='__main__':
    # 实例化登录页
    driver = webdriver.Chrome()
    l=LoginPage(driver)
    l.login()
    time.sleep(5)
    l.quit()