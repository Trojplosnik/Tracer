import sys

import requests
import subprocess
import re


def get_info(ip="192.168.1.1"):
    try:
        response = requests.get(url="http://ip-api.com/json/" + ip).json()
        if response.get('status') == "success":
            return [response.get('as').split(" ")[0],
                    response.get('country'), response.get('isp')]
        else:
            return response.get('message')
    except requests.exceptions.ConnectionError:
        print("ConnectionError")


def main():
    reg = r" {1,2}([0-9]{1,2}) .+ \[?((?:[0-9]{1,3}\.){3}[0-9]{1,3})"
    if len(sys.argv) == 2:
        print("Work in progress...", "Please wait!")
        targetIP = sys.argv[1]
        try:
            tracert_out = subprocess.check_output(f"tracert -h 15 {targetIP}",
                                                   shell=True).decode('cp866')
        except subprocess.CalledProcessError:
            print("Something wrong in subprocess tracert.\n"
                  "You may have entered a non-existent domain name or IP.")
            return
        tracertIPs = re.findall(reg, tracert_out)
        if tracertIPs:
            result = dict()
            print("N |     IP     |     AS     | COUNTRY | ISP")
            for ip in tracertIPs:
                result[ip] = get_info(ip=ip[1])
                if len(result[ip]) == 3:
                    print(f"{ip[0]} | {ip[1]} | {result[ip][0]} "
                          f"| {result[ip][1]} | {result[ip][2]}")
                else:
                    print(f"{ip[0]} | {ip[1]} | {result[ip]}")
            return result
        else:
            print("Empty trace.")
    else:
        print("Wrong input.")


if __name__ == '__main__':
    main()
