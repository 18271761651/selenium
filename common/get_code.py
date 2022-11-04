# -*- coding:utf-8 -*-
# user:Liukang
import pytesseract
from PIL import Image  # pip install pillow
from aip import AipOcr  # pip install baidu-aip
from seleniumForStudy import webdriver


class Get_code():

    # 构造函数
    def __init__(self,driver):
        self.driver=driver

    # 保存图片并进行灰度处理
    def get_code(self,xpath):

        '''获取验证码图片'''
        png = self.driver.find_element(*xpath)   #找到验证码图片所在位置
        png.screenshot('../data/capt.png')  # 将图片截屏并保存

        # 图片转灰度处理
        img = Image.open('../data/capt.png')
        img = img.convert('L')  # P模式转换为L模式(灰度模式默认阈值127)
        count = 170  # 设定阈值
        table = []
        for i in range(256):
            if i < count:
                table.append(0)
            else:
                table.append(1)
        img = img.point(table, '1')
        img.save('../data/captcha.png')  # 保存处理后的验证码

        '''验证码的识别并返回文本值'''
        APP_ID = '27998667'
        API_KEY = 'bLAhrftFmZiiAaRnCPoj5iU6'
        SECRET_KEY = '0HRzBhWx0HibQu1L45XrTa2fGXB6c8nU'
        # 初始化对象
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 读取图片
        def get_file_content(file_path):
            with open(file_path, 'rb') as f:
                return f.read()
        image = get_file_content('../data/captcha.png')
        # 定义参数变量
        options = {'language_type': 'ENG', }  # 识别语言类型，默认为'CHN_ENG'中英文混合
        #  调用通用文字识别
        result = client.basicGeneral(image, options)  # 高精度接口 basicAccurate
        # print(result)
        for word in result['words_result']:
            captcha = (word['words']).replace(" ",'').replace('\n','')
            # print('识别结果：' + captcha)
            return captcha                            # 返回验证码文本


    def demo(self):
        # 打开要识别的图片
        image = Image.open('capt.png')
        # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片，lang='chi_sim'是设置为中文识别，
        text = pytesseract.image_to_string(image, lang='chi_sim')
        # 输入所识别的文字
        print(text)

if __name__ == '__main__':
    from base_page import BasePage
    from seleniumForStudy.webdriver.common.by import By
    from seleniumForStudy.webdriver.support.ui import WebDriverWait
    from seleniumForStudy.webdriver.support import expected_conditions as ec
    from log import Logging
    # 元素
    login_url='http://hlsupply.warelucent.cc/'
    username=(By.ID,'form_item_username')
    password=(By.ID,'form_item_password')
    pictuer=(By.CLASS_NAME,'ant-image-img')
    code_box=(By.ID,'form_item_code')
    login=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/form/div[6]/div/div/div/button[1]')
    except_url='http://hlsupply.warelucent.cc/#/basic/store'
    # 记录日志
    loger = Logging().loger(level='INFO')
    driver = webdriver.Chrome()

    try:
        driver.implicitly_wait(5)
        b=BasePage(driver)

        while True:
            b.open(login_url)
            b.input(username,18271761651)
            b.input(password,123456)
            code=Get_code(driver).get_code(pictuer)
            b.input(code_box,code)
            b.click(login)
            try:
                WebDriverWait(driver,1).until(ec.url_to_be(except_url))
                loger.info(f'识别结果{code}，成功登录', )
                break
            except:
                loger.info(f'识别结果{code}，识别错误',)
                continue

    except Exception as e:
        loger.info(e)

    driver.quit()

