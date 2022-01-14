"""******* Source Code *******"""
import requests
print("requests ==", requests.__version__)

r = requests.get("http://www.google.com")
print("url:", r.url)
print("status_code:", r.status_code)
print("header:", r.headers)
print()

R = requests.get("https://raw.githubusercontent.com/sandipsahajoy/CMPUT404/main/lab-1/script.py")
print(R.text)