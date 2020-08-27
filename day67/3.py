import requests
resp = requests.post(
    url='http://httpbin.org/post',
    files={'file': open('data.xlsx', 'rb')}
)
print(resp.text)
