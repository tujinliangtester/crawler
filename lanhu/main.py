from selenium import webdriver
from bs4 import BeautifulSoup
import re, time
import requests
driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)
driver.get("https://lanhuapp.com/web/#/item/project/board?pid=151a9a0a-3100-426f-bd89-870730e57291")

time.sleep(60)

soup = BeautifulSoup(driver.page_source)
link_nodes = soup.find_all('img')
savePath='./img'
print('总共个{}'.format(len(link_nodes)))
ext_url='?x-oss-process=image/format,webp/quality,q_lossless'
for (i,link_node) in enumerate(link_nodes):
    time.sleep(1)
    print( '第{}个'.format(i+1))
    for j in range(5):
        try:
            src_url=link_node.get('src')
            #处理url 让保存的图片变成高清质量
            base_url=src_url.split('?')[0]
            src_url=base_url+ext_url
            print('src_url:',src_url)
            print("Download : %d.jpg" % ( i + 1))
            html = requests.get(src_url)
            if html.status_code == 200:
                with open(savePath + "/%d.jpg" % (i + 1), "wb") as f:
                    f.write(html.content)
                print('保存成功')
                break
            elif html.status_code == 404:
                j += 1
                time.sleep(0.05)
                continue
            else:
                print('返回异常',src_url)
        except:
            print('下载异常')
driver.close()
