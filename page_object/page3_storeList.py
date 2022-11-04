# -*- coding:utf-8 -*-
# user:Liukang
import time
import traceback
from page2_menu import Menu
from seleniumForStudy.webdriver.common.by import By
from seleniumForStudy import webdriver
import random
from seleniumForStudy.webdriver.common.keys import Keys
from seleniumForStudy.webdriver.common.action_chains import ActionChains

class StoreList(Menu):
    # 门店列表所在网址
    url='http://shop.hlwulian.com/#/basicInfo/storeList'
    # 门店名称查询输入框
    searchBox=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/header/div/div[1]/div/input')
    # 查询按钮
    storeSearchButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/header/div/div[1]/button')
    # 查询结果，默认取第一个门店名称
    def result(self,i=1):
        return self.get_txt((By.XPATH,f'//*[@id="app"]/div/div[2]/section/div[1]/div[1]/div[3]/table/tbody/tr[{i}]/td[1]/div'))
    # 添加门店按钮
    addButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/header/div/div[2]/button')
    # 审核
    def storeAuditButton(self,m=1):
        return (By.XPATH,f'//*[@id="app"]/div/div[2]/section/div[1]/div[1]/div[3]/table/tbody/tr[{m}]/td[10]/div/div/span[1]')
    # 操作项，默认编辑操作
    def editButton(self,m=1,n=1):
        '''m为门店序号，n为操作项'''
        return (By.XPATH,f'//*[@id="app"]/div/div[2]/section/div[1]/div[1]/div[3]/table/tbody/tr[{m}]/td[11]/div/button[{n}]')

    # 门店名称
    storeName=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div/input')
    # 门店编码
    storeCode=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[2]/div/div/input')
    # 同步节点
    node=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[3]/div/div/input')
    # 门店图片
    picture=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[4]/div/div/div/div')
    # 联系人
    linkMan=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[5]/div/div/input')
    # 联系电话
    phone=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[6]/div/div/input')
    # 坐标拾取
    coordinatesButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[7]/div[1]/div/*')
    # 当前坐标
    # location=(By.ID,'activePosition')
    location=(By.XPATH,'/html/body/div[8]/div[1]/div[1]')
    # 确认坐标
    ensure=(By.XPATH,'/html/body/div[1]/div/div[2]/section/div[1]/div[6]/div/div/div[3]/span/button[2]')
    # 地区选择框
    eraBox=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[7]/div[2]/div/div/div/input')
    # 选择地区（省市区）
    def chooseEra(self,p=17,c=1,e=8):
        province=(By.XPATH,f'/html/body/div[3]/div[1]/div/div[1]/ul/li[{p}]')
        city=(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[{c}]')
        era=(By.XPATH,f'/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[{e}]')
        for i in (province,city,era):
            self.drop_list_choose(i)
    # 详细地址
    address=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[8]/div/div/input')
    # 备注
    remark=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[2]/div/form/div[9]/div/div/textarea')
    # 门店介绍（表单）
    iframe=(By.ID,'tiny-vue_29843026121648908212920_ifr')
    # 门店介绍（文本框）
    introduction=(By.XPATH,'//*[@id="tinymce"]')
    # 保存按钮
    saveButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[3]/div/div[3]/span/button')

    # 添加管理员
    # 姓名搜索框
    adminNameBox=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[1]/div[1]/input')
    # 手机搜索框
    adminPhoneBox=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[1]/div[2]/input')
    # 管理员查询按钮
    adminSearchButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[1]/button')
    # 管理员添加按钮
    adminAddButton=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[1]/div[2]/button')
    # 管理员审核
    adminAudit=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div/div/span[1]')
    # 手机退款权限
    phoneRefund=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div/div/span[1]')
    # 是否分拣员
    isSorter=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div/div/span[1]')
    # 管理员操作项目 1修改、2删除、3充值密码、4绑定微信
    def editAdminButton(self,i):
        return (By.XPATH,f'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[1]/div/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/button[{i}]')
    # 管理员登录名
    adminUN = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[2]/div/form/div[2]/div/div/input')
    # 管理员密码
    adminPW = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[2]/div/form/div[3]/div/div/input')
    # 重复管理员密码
    repeadPW=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[2]/div/form/div[4]/div/div/input')
    # 管理员姓名
    adminName=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[2]/div/form/div[5]/div/div/input')
    # 管理员手机号
    adminPhone=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[2]/div/form/div[6]/div/div/input')
    alertEnsure=(By.XPATH,'/html/body/div[2]/div/div[last()]/button[2]')
    # 确认添加管理员按钮
    addAdminEnsure=(By.XPATH,'//*[@id="app"]/div/div[2]/section/div[1]/div[4]/div[2]/div/div[3]/span/button[2]')

    # 门店查询
    def searchStore(self,storename=''):
        self.open(self.url)
        self.input(self.searchBox,storename)
        self.click(self.storeSearchButton)
    # 门店添加、修改
    def store(self,
                 operation='add',
                 name=f'API{int(random.uniform(10000,99999))}',
                 code=f'{int(random.uniform(10000,99999))}',
                 node='api',
                 linkman='api',
                 phone=f'1827{int(random.uniform(1000000,9999999))}',
                 address='光谷科技港5栋',
                 remark='api',
                 introduction='api'):
        if operation=='add':
            self.open(self.url)
            self.click(self.addButton)
        elif operation=='edit':
            self.click(self.editButton())
            # 选择地区
        else:
            print('操作不存在')
        # 基础信息
        self.input(self.storeName,name)
        self.input(self.storeCode,code)
        self.input(self.node,node)
        self.input(self.linkMan,linkman)
        self.input(self.phone,phone)
        self.input(self.address, address)
        self.input(self.remark, remark)
        # 选择门店坐标
        self.click(self.coordinatesButton)
        self.switch_frame('mapPage')
        # loading状态等待1s
        while self.driver.find_element(By.XPATH,'/html/body/div[1]').is_displayed():
            time.sleep(0.5)
        self.click(self.location)
        self.driver.switch_to.default_content()
        self.click(self.ensure)
        # 选择地区
        self.click(self.eraBox)
        self.chooseEra()
        # 门店介绍
        time.sleep(0.5), self.switch_frame(0)
        self.input(self.introduction, introduction)
        self.driver.switch_to.default_content()
        # 保存
        self.click(self.saveButton)
    # 门店审核
    def storeAudit(self):
        self.click(self.storeAuditButton())

    # 管理员添加
    def addAdministrator(self,usermane=f'api{int(random.uniform(101,999))}',pw=123456,name='',phone=''):
        # self.open(self.url)
        self.click(self.editButton(1,2))
        self.click(self.adminAddButton)
        self.input(self.adminUN,usermane)
        self.input(self.adminPW,pw)
        self.input(self.repeadPW,pw)
        self.input(self.adminName,name)
        self.input(self.adminPhone,phone)
        self.click(self.addAdminEnsure)
    # 管理员查询
    def searchAdmin(self,name='',phone=''):
        self.open(self.url)
        self.editButton(1,2)
        self.input(self.adminNameBox,name)
        self.input(self.adminPhoneBox,phone)
        self.click(self.adminSearchButton)
    # 管理员启用并授权
    def grantAuthority(self):
        self.click(self.adminAudit)
        self.click(self.phoneRefund)
        self.click(self.isSorter)
    # 删除管理员
    def deleteAdmin(self):
        self.searchAdmin()
        self.click(self.editAdminButton(2))
        self.click(self.alertEnsure)
    # 重置密码
    def resetPassword(self):
        self.searchAdmin()
        self.click(self.editAdminButton(3))
        self.click(self.alertEnsure)



if __name__ == '__main__':
    try:
        s = StoreList()
        # 登录后台
        s.login()
        # 添加门店
        s.store('add')
        print(s.tipsTxt())
        s.driver.refresh(), s.switch_alert().accept()
        # 查询门店
        s.searchStore()
        # 编辑门店
        s.store('edit')
        print(s.tipsTxt())
        s.driver.refresh(),s.switch_alert().accept()
        '''# 根据文件内容添加、修改门店
        file = 'C:/Users/Administrator/Desktop/testDocument/store.xlsx'
        # 查询门店并进入编辑
        for i in s.read_excel(file,0,1):
            s.searchStore(i[1])
            s.store('edit',*i)
            print(s.tipsTxt())
            # 刷新页面，并处理系统弹窗
            s.driver.refresh(),s.switch_alert().accept()'''
        # 审核门店
        s.storeAudit(),print(s.tipsTxt())
        s.storeAudit(),print(s.tipsTxt())
        # 添加门店管理员
        s.addAdministrator(),print(s.tipsTxt())

    except Exception as e:
        print(e)
    finally:
        s.quit()
        pass
