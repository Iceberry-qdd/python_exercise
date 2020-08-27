import requests
resp = requests.get('http://github.com', timeout=0.01)
print(resp.status_code)
