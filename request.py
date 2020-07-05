# _*_ coding: utf-8 _*_
# @Time    :2020/7/2
# @Author  :lemon_yuehaulong
# @Email    :374748859@qq.com
import requests
def http_request(url,data,token=None,method='post'):  #注册和登陆的函数
    header= {'X-Lemonban-Media-Type': 'lemonban.v2', 'Authorization':token}
    if method=='get':
        result=requests.get(url,json=data,headers=header)
    else:
        result = requests.post(url, json=data, headers=header)
    return result.json()    #这一步很重要
if __name__ == '__main__':

    #登陆

    login_url = 'http://120.78.128.25:8766/futureloan/member/login'
    login_data = {'mobile_phone': '15220597312', 'pwd': 'lemon666'}
    print(http_request(login_url,login_data))
    response=http_request(login_url,login_data,)
    token =response['data']['token_info']['token']
    #充值
    header_2={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':'Bearer '+token}
    recharge_url='http://120.78.128.25:8766/futureloan/member/recharge'
    recharge_data={'member_id':'206698','amount':5000}
    print(http_request(recharge_url,recharge_data,'Bearer '+token))
