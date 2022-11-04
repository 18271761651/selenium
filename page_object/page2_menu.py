from page1_login import LoginPage
from seleniumForStudy.webdriver.common.by import By
from seleniumForStudy import webdriver

class Menu(LoginPage):
    # 成功提示
    tips = (By.XPATH,'/html/body/div[last()]/div/h2')
    # 错误提示
    message = (By.XPATH, f'/html/body/div[last()]/p')

    # 选择一二级菜单
    def choosePage(self,m,n):
        # 一级菜单
        page = (By.XPATH, f'//*[@id="app"]/div/div[1]/nav/div[1]/div/div[1]/div/div[{m}]')
        # 二级菜单
        second_page = (By.XPATH, f'//*[@id="app"]/div/div[1]/nav/div[{m}]/div/div[1]/div/div[{n}]')
        # 选择一级菜单
        self.click(page)
        # 选择二级菜单
        self.click(second_page)

    # 获取操作提示信息
    def tipsTxt(self):
        try:
            txt=self.get_txt(self.tips)
        except:
            txt=self.get_txt(self.message)
        finally:
            return txt


if __name__ == '__main__':
    driver=webdriver.Chrome()
    m=Menu(driver)
    m.login('lleg',123456)
    m.choosePage(2,2)
    m.quit()