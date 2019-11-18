import requests

r = requests.get('https://www.python.org')

print(r.status_code)

print(" ")

print(r.headers)

print(" ")

print(r.cookies)

print(" ")

print(r.encoding)

