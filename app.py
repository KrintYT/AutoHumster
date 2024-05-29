import requests
import time

url = "https://api.hamsterkombat.io/clicker/tap"
headers = {
    "Host": "api.hamsterkombat.io",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "",
    "Origin": "https://hamsterkombat.io",
    "Referer": "https://hamsterkombat.io/",
    "Connection": "keep-alive"
}

payload = {
    "count": ,
    "availableTaps": ,
    "timestamp": 
}

while True:
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status Code: {response.status_code}")
    time.sleep()  
