from selenium import webdriver
from bs4 import BeautifulSoup
import re, time

from bs4.element import Tag
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# dblist = myclient.list_database_names()
# print(dblist)
mydb = myclient["NationalDayOnWeiBo"]

# MongoDB 使用数据库对象来创建集合
mycol = mydb["NationalDayOnWeiBoSet"]


driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)

driver.get("https://weibo.com/")
# 手动登录，搜索关键字，并且手动跳转到第二页
print('1.登录；\n2.搜索；\n3.跳转到第二页')

i=0
while True:
    if(i>60):break
    i+=1
    print(i,end='')
    time.sleep(1)
    print('\r',end='',flush=True)

i = 0
while (True):
    if(i>10000):break
    time.sleep(3)
    list=[]
    i+=1
    soup = BeautifulSoup(driver.page_source)
    link_nodes = soup.find_all('p', {'node-type':'feed_list_content'})
    for link_node in link_nodes:
        dic = {}
        feed_list_content = link_node.get_text().strip()
        nickname=link_node.get('nick-name')

        print(feed_list_content)
        print(nickname)
        dic['nickname']=nickname
        dic['feed_list_content']=feed_list_content
        list.append(dic)

    mycol.insert_many(list)
    if(i%50==0):time.sleep(600)
    # 下一页
    driver.find_element_by_link_text(u"下一页").click()



time.sleep(5)
# driver.close()
