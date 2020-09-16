from selenium import webdriver
from bs4 import BeautifulSoup
import re, time
import requests
import csv, asyncio

base_url = 'https://time.geekbang.org/serv/v1/'
product_url = base_url + 'my/products/all'

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
# driver.implicitly_wait(30)
driver.set_page_load_timeout(120)



def count_down(n):
    # 打印倒计时
    for x in range(n, -1, -1):
        mystr = "count down:" + str(x) + "s"
        print("\r倒计时%s" % mystr, end="")
        time.sleep(1)


def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

# /////////////////////////////////延时异步//////////////////////////////////////////////


async def myAsync(loop,callback1,url,callback2):
    print('registering callbacks')
    if(url is None):
        loop.call_later(1, callback1)
    else:
        loop.call_later(1,callback1,url)
    loop.call_later(1,count_down,30)
    #默认超时是30秒
    loop.call_later(30, callback2)
    await asyncio.sleep(30)


# try:
#     print('entering event loop')
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     print('closing event loop')
#     event_loop.close()

# /////////////////////////////////延时异步结束//////////////////////////////////////////////

def myWindowStop():
    print('myWindowStop')
    driver.execute_script('window.stop()')

try:
    print('手动登录')
    driver.get("https://account.geekbang.org")
except Exception:
    print(Exception)
    myWindowStop()

count_down(30)

try:
    print('手动关闭弹窗')
    driver.get('https://time.geekbang.org/')
except Exception:
    print(Exception)
    myWindowStop()

count_down(30)

els = driver.find_elements_by_class_name('_20Cq3Rn7_0')
for el in els:
    print(el)
    try:
        el.click()
    except Exception:
        print(Exception)
        myWindowStop()
    driver.switch_to.window(driver.window_handles[-1])
    count_down(60)

    els2 = driver.find_elements_by_class_name('_2NgRM2G9_0')
    for index_el2,el2 in enumerate(els2):
        print('el2 ',el2)
        if(index_el2>0):
            el2.click()
            count_down(2)

        els3 = driver.find_elements_by_class_name('_3DJrlH2u_0')
        for el3 in els3:
            print('el3',el3)
            file_name = validateTitle(el3.get_attribute('innerText'))
            el3.click()
            count_down(20)

            # soup = BeautifulSoup(driver.page_source)
            # content=soup.find('div', class_="_1kh1ihh6_0").get_text().strip()
            # print('content:'+content)
            with open(file_name, 'wb') as f:
                f.write(driver.page_source.encode("gbk", "ignore"))
                print('写入文件成功')

driver.close()
