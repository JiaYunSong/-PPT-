import os
import requests


def getImage(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        if r.status_code != 200:
            raise Exception(f"code={r.status_code}")
        return r.content
    except Exception as e:
        print(f"Request ERROR: {e} // URL: {url}")
        exit(0)


f = open(r"source.txt", 'r', encoding='utf-8')
source = f.read()
source = source[source.find('= \"'):source.find('\";')][3:]
img_path = source.replace('\n', '').split(',')

if not os.path.exists('img'):
    os.mkdir('img')

for i in range(len(img_path)):
    r = requests.get(img_path[i])
    img = r.content
    with open(f'img/{i}.png', 'wb') as f:
        f.write(img)
    print(f"第{i}页完成获取")

# 不用尝试多线程，速度一样烂
