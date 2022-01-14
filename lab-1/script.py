import requests
print("requests ==", requests.__version__)
r = requests.get("http://www.google.com")
print(r.url)
print(r.status_code)
print(r.headers)

R = requests.get("https://raw.githubusercontent.com/sandipsahajoy/CMPUT404/main/lab-1/script.py")
print(R.text)