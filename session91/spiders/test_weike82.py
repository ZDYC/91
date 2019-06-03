import requests


id = '37562'
code_url = 'http://www.weike59.com/common/getcode.asp'
login_url = 'http://www.weike59.com/users/login.asp?action=login'
url = 'http://www.weike50.com/show.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}


session = requests.Session()
session.headers.update(headers)


code_res = session.get(code_url)
with open('code.png', 'wb') as f:
    f.write(code_res.content)

code = input('code:::')
data = {
    'username': 'cuijie0604',
    'password': 'cuijie0604',
    'checkcode': code,
    'x': '57',
    'y': '21'
}
login_res = session.post(login_url, data=data)
# print(session.cookies)
print(requests.utils.dict_from_cookiejar(session.cookies))
res = session.get(url, params={'id': id})
print(res, res.text)