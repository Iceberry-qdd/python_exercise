import requests


cookies = {'key1': 'value1', 'key2': 'value2'}
resp = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(resp.text)
print('*'*20)
jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
jar.set('tasty_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
resp = requests.get('http://httpbin.org/cookies', cookies=jar)
print(resp.text)
