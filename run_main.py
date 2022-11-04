# -*- coding:utf-8 -*-
# user: Liukang

import os
import unittest
from POM.common.send_report import Report
from POM.common.log import Logging

# 返回项目目录（Unittest）
path =os.path.dirname(__file__)+'/test_cases'
# 生成测试集
suite = unittest.TestLoader().discover(path, pattern='test*.py')

if __name__ == "__main__":
    # 运行测试集、生成报告并发送邮件
    logger=Logging().loger("INFO")
    try:
        Report.report_email(suite, "POM")
        logger.info('自动化测试报告发送成功 !')
    except Exception as e:
        logger.error(e)
