# -*- coding: utf-8 -*-

from API_test.common.basecheck import BaseCheck

base_url = 'http://192.168.7.227:8080/zhigou/'

CHECK_CODE = 'P_Merchant__CheckCode'  # 检查组织机构代码
CHECK_NAME = 'P_Merchant__CheckName'  # 检查单位名
GET_APPLY_LIST = 'P_Merchant__GetApplyList'  # 获取商户资料
CHECK_MOBILE = 'P_User__GetMobile'  # 检查手机号
GET_AREA = 'P_User__GetArea'  # 获取所在地
ADD_STEP1 = 'P_Merchant__AddStep1'  # 添加商户第1步
ADD_STEP2 = 'P_Merchant__AddStep2'  # 添加商户第2步
ADD_STEP3 = 'P_Merchant__AddStep3'  # 添加商户第3步
GET_BASIC_STATUS = 'P_Merchant__GetBasicStatus'  # 获取商户状态
OPEN_SHOP = 'P_Merchant__OpenShop'  # 开通店铺
ADD_USER = 'P_User__AddUser'  # 用户注册
GET_USER_PASSWORD_INFO = 'P_User__GetUserPasswordInfo'  # 验证密码
BIND_BEST = 'R_Bind__User'  # 绑定best
UNBIND_BEST = 'R_UnBind__User'  # 解绑best

# 1.检查组织机构代码api
# docheck(base_url + CHECK_CODE, 'check.xlsx', 'CheckCode')
# 2.检查企业名称api
# docheck(base_url + CHECK_NAME, 'check.xlsx', 'CheckName')
# 3.获取商家入驻申请资料api
# docheck(base_url + GET_APPLY_LIST, 'check.xlsx', 'GetApplyList')
# 4.检查手机号api
# docheck(base_url + CHECK_MOBILE, 'check.xlsx', 'GetMobile')
# 5.获取所在地api
# docheck(base_url + GET_AREA, sheet_name='GetArea')
# 6.添加商户第一步api
# docheck(base_url + ADD_STEP1, sheet_name='AddStep1')
# 7.添加商户第二步api
# docheck(base_url + ADD_STEP2, sheet_name='AddStep2')
# 8.添加商户第三步api
# docheck(base_url + ADD_STEP3, sheet_name='AddStep3')
# 9.获取商户状态api
# docheck(base_url + GET_BASIC_STATUS, sheet_name='GetBasicStatus')
# 10.开通商铺api
# docheck(base_url + OPEN_SHOP, sheet_name='OpenShop')
# 11.用户注册api
# docheck(base_url + ADD_USER, sheet_name='AddUser')
# 12.验证密码api
# docheck(base_url + GET_USER_PASSWORD_INFO, sheet_name='GetUserPasswordInfo')
# 13.绑定best api
results = BaseCheck(base_url + BIND_BEST, sheet_name='Bind').docase()
for case in results:
    print case['params'], case['response']
# 14.解绑best api
# docheck(base_url + UNBIND_BEST, sheet_name='UnBind')

