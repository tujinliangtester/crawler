from selenium import webdriver
from bs4 import BeautifulSoup
import re, time
import requests
import csv, asyncio
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


base_url = 'https://time.geekbang.org/serv/v1/'
product_url = base_url + 'my/products/all'

#get直接返回，不再等待界面加载完成
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"

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

def myWindowStop():
    print('myWindowStop')
    # driver.execute_script('XMLHttpRequest.abort()')
    driver.execute_script('window.stop()')


#  注意，这个网站中，可能涉及到页面跳转的，都会有浏览器一直加载的问题，需要特别留意，
#  而对于点击后仍然处于当前页面的，应该可以不用等待太久
def count_down_and_stop(n):
    count_down(n)
    # myWindowStop()

driver.get("https://account.geekbang.org")
print('登录，进入列表页，并且关闭弹窗')
count_down(180)
driver.switch_to.window(driver.window_handles[-1])
# myWindowStop()
print('确认是否需要手动停止窗口！')
els = driver.find_elements_by_class_name('_20Cq3Rn7_0')
for el in els:
    print(el)
    el.click()
    driver.switch_to.window(driver.window_handles[-1])
    count_down_and_stop(20)

    els2 = driver.find_elements_by_class_name('_2NgRM2G9_0')
    for index_el2,el2 in enumerate(els2):
        print('el2 ',el2)
        if(index_el2>0):
            el2.click()
            count_down(2)
        els3 = driver.find_elements_by_class_name('_3DJrlH2u_0')
        for el3 in els3:
            print('el3',el3)
            file_name = validateTitle(el3.get_attribute('innerText'))+'.html'
            el3.click()
            count_down(20)

            # soup = BeautifulSoup(driver.page_source)
            # content=soup.find('div', class_="_1kh1ihh6_0").get_text().strip()
            # print('content:'+content)
            with open(file_name, 'wb') as f:
                f.write(driver.page_source.encode("utf8"))
                print('写入文件成功')

driver.close()
