import requests
resp = requests.get('http://www.taobao.com', proxies={
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10.1080',
})
print(resp.status_code)
