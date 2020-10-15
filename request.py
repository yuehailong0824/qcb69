# _*_ coding: utf-8 _*_
# @Time    :2020/7/2
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
import requests
def http_request(url,data,token=None,method='post'):
    header= {'X-Lemonban-Media-Type': 'lemonban.v2', 'Authorization':token}
    if method=='post':
        result=requests.post(url,json=data,headers=header)
    else:
        result = requests.get(url, json=data, headers=header)
    print(result.json())
    return result.json()
if __name__ == '__main__':
    login_url = 'http://120.78.128.25:8766/futureloan/member/login'
    login_data = {'mobile_phone': '15220597312', 'pwd': 'lemon666'}
    response=http_request(login_url,login_data)

    token = response['data']['token_info']['token']
    recharge_url='http://120.78.128.25:8766/futureloan/member/recharge'
    recharge_data={'member_id':'16907','amount':100}
    http_request(recharge_url,recharge_data,'Bearer '+token)
