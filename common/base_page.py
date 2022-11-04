# -*- coding:utf-8 -*-
# user:Liukang

import time

import xlrd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class BasePage():
    # 调用浏览器

    driver = webdriver.Chrome()
        # 调试模式
        # cmd启动浏览器：chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"
        # options = Options()
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        # browser=webdriver.Chrome(options=options)

    # 访问域名
    def open(self, url):
        self.driver.get(url)

    # 显示等待
    def show_wait(self, loc, time=5):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(loc))

    # 定位元素，高亮显示
    def locator(self, loc):
        style = "background: green; border: 2px solid red;"  # 高亮的样式
        self.show_wait(loc)
        element = self.driver.find_element(*loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)
        return element

    # 切换至提示框
    def switch_alert(self, time=5):
        WebDriverWait(self.driver, time).until(ec.alert_is_present())
        return self.driver.switch_to.alert

    # 定位表单
    def switch_frame(self, frame):
        WebDriverWait(self.driver,time).until(ec.frame_to_be_available_and_switch_to_it(frame))

    # 回车
    def enter(self, loc):
        self.locator(loc).send_keys(Keys.ENTER)

    # 单击
    def click(self, loc):
        ActionChains(self.driver).click(self.locator(loc)).perform()

    # 双击
    def double_click(self, loc):
        ActionChains(self.driver).double_click(self.locator(loc)).perform()

    # 输入文本
    def input(self, loc, txt):
        self.clear(loc)
        self.locator(loc).send_keys(txt)

    # 获取文本
    def get_txt(self, loc):
        return self.locator(loc).text

    # 鼠标悬浮
    def move_to(self, element):
        ActionChains(self.driver).move_to_element(self.locator(element)).perform()

    # 清除内容
    def clear(self, textera):
        self.locator(textera).clear()

    # 选择下拉列表内容
    def drop_list_choose(self,loc):
        self.driver.execute_script('arguments[0].click();',self.locator(loc))

    # 等待跳转
    def url_to_be(self,url):
        WebDriverWait(self.driver,5).until(ec.url_to_be(url))

    # 关闭webdriver
    def quit(self):
        self.driver.quit()

    # 读取excel文件
    def read_excel(self, filename, sheetindex, read_from_row):
        excel = xlrd.open_workbook(filename, on_demand=True)
        sheet = excel.sheets()[sheetindex]
        contents = [sheet.row_values(i) for i in range(read_from_row, sheet.nrows)]
        return contents

if __name__ == '__main__':
    b = BasePage()
    # b.open("https://www.baidu.com")
    # b.input((By.ID, "kw"),1233)
    # b.click((By.ID, "su"))
    # time.sleep(3)
    # b.quit()
