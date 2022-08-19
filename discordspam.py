import os
import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = 'https://applicationhypetest.cf/login/'

names = open('C:/Users/Rayyan/OneDrive/Desktop/temp/nameslist.json')
data = json.load(names)

for name in data:
    name_extra = ''+(random.choice(string.digits))
    name=(name.lower())
    
    #email_domain = ['@gmail.com','@yahoo.com''@outlook.com','@live.com','@icloud.com','@aol.com']

    username = name + name_extra + '@gmail.com'
    print(username)
    password = ''.join(random.choice(chars) for i in range(8))
    print(password)
    requests.post(url, allow_redirects=False, data={
    'username': username,
    'password': password
    })
