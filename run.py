# _*_ coding: utf-8 _*_
# @Time    :2020/7/3
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
#执行文件
from read_data import read_data
from request import http_request
#第一步 获取到测试数据
all_case=read_data('text_shuju_1.xlsx','Sheet1')
# print('获取到的数据为：',all_case_1)
#第二步 执行测试
print('第一条用例的数据：',all_case[0])
login_data=all_case[0]
ip="http://120.78.128.25:8766"
login_response=http_request(ip+login_data[4],eval(login_data[5]),token=None,method=login_data[3])
print(login_response)
for i in range(1,len(all_case)):
    test_data=all_case[i]
    expected=eval(test_data[6])
    token = login_response['data']['token_info']['token']
    # ip="http://120.78.128.25:8766"
    response=http_request(ip+test_data[4],eval(test_data[5]),'Bearer '+token,method=test_data[3])
    print("最后的结果是：",response)
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")