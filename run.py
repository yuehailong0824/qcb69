# _*_ coding: utf-8 _*_
# @Time    :2020/7/3
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
#执行文件
from read_data import read_data
from request import http_request
# 方法一
# # 步骤一：获取到测试数据
# all_case=read_data('text_shuju_1.xlsx','Sheet1')
# #步骤二：执行测试先登陆
# print('第一条用例的数据{}'.format(all_case[0]))
# uri="http://120.78.128.25:8766"
# login_data=all_case[0]
# login_response=http_request(uri+login_data[4],eval(login_data[5]),token=None,method=login_data[3])
# token = login_response['data']['token_info']['token']
# #充值
# for i in range(1,len(all_case)):
#     test_data=all_case[i]
#     http_request(uri+test_data[4],eval(test_data[5]),'Bearer '+token,method=test_data[3])
# 方法二
Token=None
def run(file_name,sheet_name):
    global Token   #申明函数内外的Token值相同
    all_case=read_data(file_name,sheet_name)
    for test_data in all_case:
        uri = "http://120.78.128.25:8766"
        response=http_request(uri+test_data[4],eval(test_data[5]),token=Token,method=test_data[3])
        if 'login' in test_data[4]:
            Token='Bearer '+response['data']['token_info']['token']
run('text_shuju_1.xlsx','Sheet1',)

