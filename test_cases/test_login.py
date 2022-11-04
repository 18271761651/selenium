# -*- coding:utf-8 -*-
# user:Liukang

from POM.page_object.page1_login import LoginPage
import unittest
from POM.common.log import Logging
from POM.common.my_util import Myutil


class TestLogin(Myutil,LoginPage):

    # @file_data('../data/user_data/')
    def test_01_login(self):
        '''登录'''
        username='lleg'
        password=123456
        self.login(username,password)
        exc='http://shop.hlwulian.com/#/dashboard'
        act=self.driver.current_url
        self.assertEqual(exc,act,msg=act)



if __name__ == '__main__':
    try:
        unittest.TestCase()
    except Exception as e:
        Logging().loger().error(e)

