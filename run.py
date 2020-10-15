# _*_ coding: utf-8 _*_
# @Time    :2020/7/3
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
#执行文件
from read_data import read_data
from http_request import http_request
Token=None
def run(file_name,sheet_name):
    global Token   
    all_case=read_data(file_name,sheet_name)
    for test_data in all_case:
        uri = "http://120.78.128.25:8766"
        response=http_request(uri+test_data[4],eval(test_data[5]),token=Token,method=test_data[3])
        if 'login' in test_data[4]:
            Token='Bearer '+response['data']['token_info']['token']
run('text_shuju_1.xlsx','Sheet1',)

