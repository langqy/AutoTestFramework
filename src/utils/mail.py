# -*- coding: utf-8 -*-
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.utils.config import DefaultConfig
from src.utils.logger import Logger


class Email:
    """Email类，读取配置中的基本配置，初始化要求title必填，message与文件路径可选"""
    def __init__(self, title, message=None, path=None):
        """调用DefaultConfig类，读取配置"""
        self.logger = Logger(__name__).return_logger()

        self.title = title
        self.message = message
        self.files = path

        cf = DefaultConfig()
        self.server = cf.get('email', 'server')
        self.sender = cf.get('email', 'from')
        self.receiver = cf.get('email', 'to')
        self.password = cf.get('email', 'pass')

        self.msg = MIMEMultipart('related')

    def _attach_file(self, att_file):
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        filename = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % filename[-1]
        self.msg.attach(att)

    def send(self):
        """发送邮件"""

        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 附上文件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        # todo: log, 优化
        try:
            smtp_server = smtplib.SMTP(self.server)
            smtp_server.login(self.sender, self.password)
            smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            self.logger.info(u'发送邮件\'%s\'成功!' % self.title)
        except Exception as e:
            self.logger.error(e)
        finally:
            smtp_server.quit()


if __name__ == '__main__':
    tit = u'测试报告'
    tex = '这是今天的测试报告！请查看'
    # f = 'D:\\py\\1.py'
    import os
    p = DefaultConfig().get('path', 'report')
    newestfile = sorted([(x, os.path.getctime(os.path.join(p, x))) for x in os.listdir(p) if os.path.isfile(os.path.join(p, x))], key=lambda i: i[1])[-1]
    filename = p + newestfile[0]
    print filename
    # import datetime
    # filename = DefaultConfig().get('report', 'path') + 'report-{0}.html'.format(datetime.date.today())
    email = Email(title=tit, message=tex, path=[filename, 'D:\\baidu.py'])
    email.send()