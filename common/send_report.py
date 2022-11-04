# -*- coding:utf-8 -*-
# user:Liukang
import os.path
import smtplib
import time
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText


class Report(object):

    # 邮件发送最新HTML测试报告
    def report_email(suite, title):
        # 获取当前时间
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        # 报告存放路径
        report_path = os.getcwd() + '/test_report/'
        # 执行测试集、生成测试报告
        HTMLFile = report_path + now + 'api.html'
        # with open(HTMLFile,'wb') as fp:
        try:
            fp = open(HTMLFile, 'wb')
            runner = HTMLTestRunner(stream=fp, title=title, description=u"用例执行情况")
            runner.run(suite)
            fp.close()
            print("报告已生成：%s" % HTMLFile)

            # 获取最新报告
            try:
                lists = os.listdir(report_path)
                lists.sort(key=lambda fn: os.path.getatime(report_path + "\\" + fn))
                file_new = os.path.join(report_path, lists[-1])
                print("已获取最新测试报告：" + file_new)
                # 发送邮件
                try:
                    f = open(file_new, 'rb')
                    mail_body = f.read()
                    f.close()
                    msg = MIMEText(mail_body, 'html', 'utf-8')
                    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
                    msg['Subject'] = Header("自动化测试报告" + rq, 'utf-8')

                    try:
                        smtp = smtplib.SMTP()
                        smtp.connect("smtp.qq.com")
                        smtp.login("1661289226@qq.com", "fztwjhnxyveydgad")
                        smtp.sendmail("1661289226@qq.com", "1445034070@qq.com", msg.as_string())
                        smtp.quit()
                        print('自动化测试报告发送成功 !')
                    except Exception as e:
                        print("测试报告发送失败 ！" + e)
                        return e
                except Exception as e:
                    print(e)
                    return e
            except Exception as e:
                print("最新报告获取失败 ！" + e)
                return e
        except Exception as e:
            print("报告生成失败 ！" + e)
            return e

