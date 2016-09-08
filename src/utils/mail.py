# -*- coding: utf-8 -*-
"""发送Email。

class:

Email  -- 发送Email给指定用户，可带附件，通常可用于发送测试报告等。

    methods:

        __init__  -- 初始化Email类，读取配置或输入，获得邮件标题、发件人、收件人、附件等

        send  -- 发送Email。

"""
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass
from socket import gaierror, error

from src.utils.config import DefaultConfig
from src.utils.logger import Logger
from src.utils.utils_exception import NoOptionError


class Email:
    """Email类，读取配置中的基本配置，初始化要求title必填，message与文件路径可选"""

    def __init__(self, title, message=None, path=None, server=None, sender=None, password=None, receiver=None):
        """初始化Email

        :param title: 邮件标题，必填。
        :param message: 邮件正文，非必填。
        :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        :param server: smtp服务器，如果为空，则读取config.ini中的[email]/server，非必填。
        :param sender: 发件人，如果为空，则读取config.ini中的[email]/from，非必填。
        :param password: 发件人密码，如果为空，则读取config.ini中的[email]/password，如果读取失败，则需手动输入密码，非必填。
        :param receiver: 收件人，如果为空，则读取config.ini中的[email]/to，多收件人用“；”隔开，非必填。
        """
        self.logger = Logger(__name__).return_logger()

        self.title = title
        self.message = message
        self.files = path

        self.msg = MIMEMultipart('related')

        cf = DefaultConfig()
        if server:
            self.server = server
        else:
            self.server = cf.get('email', 'server')

        if sender:
            self.sender = sender
        else:
            self.sender = cf.get('email', 'from')

        if receiver:
            self.receiver = receiver
        else:
            self.receiver = cf.get('email', 'to')

        if password:
            self.password = password
        else:
            try:
                self.password = cf.get('email', 'pass')
            except NoOptionError:
                self.password = getpass(prompt=u'未在config.ini中检测到password，请输入password： ')

    def _attach_file(self, att_file):
        """内部方法，将单个文件添加到附件列表中"""
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        filename = re.split(r'[\\|/]', att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % filename[-1]
        self.msg.attach(att)
        self.logger.info('attach file {}'.format(att_file))

    def send(self):
        """组织邮件内容并发送邮件。"""

        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        # 邮件正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        # 添加附件，支持多个附件（传入list），或者单个附件（传入str）
        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        # 连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror and error) as e:
            self.logger.exception(u'发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                self.logger.exception(u'用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp_server.quit()
                self.logger.info(u'发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                                 u'同时检查收件人地址是否正确'.format(self.title, self.receiver))


if __name__ == '__main__':
    tit = u'测试报告'
    tex = '这是今天的测试报告！请查看'
    p = DefaultConfig().get('path', 'report')
    from src.utils.support import get_newest_file_of_path
    newestfile = get_newest_file_of_path(p)
    filename = p + newestfile[0]
    print filename
    email = Email(title=tit, message=tex, path=[filename])
    email.send()