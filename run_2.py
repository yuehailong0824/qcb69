# _*_ coding: utf-8 _*_
# @Time    :2020/7/3
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
#7月1号后半小时课程需要复看
from ceshiyong.read_data import read_data
from ceshiyong.request import http_request
from openpyxl import load_workbook
Token=None   #全局变量
def run():
    global Token    #在这里申明，函数外的Token和函数内的Token是同一个值
    all_case=read_data('text_shuju_1.xlsx','Sheet1')
    print('第一条用例的数据：',all_case[0])
    for i in range(len(all_case)):
        test_data=all_case[i]
        ip = "http://120.78.128.25:8766"
        response = http_request(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
        if 'login' in test_data[4]:
            Token = "Bearer "+response['data']['token_info']['token']
        print("最后的结果是：",response)
        #开始写入结果
        wb=load_workbook('text_shuju_1.xlsx')
        sheet=wb['Sheet1']
        sheet.cell(row=test_data[0]+1,column=8).value=str(response)
        actual={'code':response['code'],'msg':response['msg']}
        print(actual)
        if eval(test_data[6])==actual:
            print('测试通过')
            sheet.cell(row=test_data[0]+1,column=9).value='PASS'
        else:
            print('测试不通过')
            sheet.cell(row=test_data[0]+1,column=9).value='FAIL'
        wb.save('text_shuju_1.xlsx')

run()