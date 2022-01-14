import requests
print("requests ==", requests.__version__)
r = requests.get("http://www.google.com")
print(r.url)
print(r.status_code)
print(r.headers)