from selenium import webdriver
from bs4 import BeautifulSoup
import re, time

from bs4.element import Tag
import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "123456", "muorie")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

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
    if(i>10):break
    time.sleep(3)
    list=[]
    i+=1
    soup = BeautifulSoup(driver.page_source)
    link_nodes = soup.find_all('div', {'action-type':'feed_list_item'})
    for link_node in link_nodes:
        dic = {}
        nickname=link_node.find('a',{'class':'name'}).get_text().strip()
        dic['nickname']=nickname

        feed_list_content = link_node.find('p',{'node-type':'feed_list_content'}).get_text().strip()
        dic['feed_list_content']=feed_list_content

        site_detail=link_node.find('p',{'node-type':'feed_list_content'}).find_all('a')
        if(len(site_detail)>0):
            site_detail=site_detail[-1]
            site_detail_i=site_detail.find('i')
            if(site_detail_i is not None):
                if(site_detail.find('i').get_text().strip()=='2'):
                    site_detail=site_detail.get_text().strip()
                    dic['site_detail'] = site_detail[1:]

        feed_list_media_prev=link_node.find('div',{'node-type':'feed_list_media_prev'})
        if(feed_list_media_prev is not None):
            img_src_strs=''
            imgs=feed_list_media_prev.find_all('img')
            for img in imgs:
                img_src_strs+=','+img.get('src')
            dic['feed_list_media_prev']=img_src_strs

        fl_h5_video_disp=link_node.find('div',{'node-type':'fl_h5_video_disp'})
        if(fl_h5_video_disp is not None):
            src=fl_h5_video_disp.find('video')
            if(src is not None):
                src=src.get('src')
            dic['fl_h5_video_disp']=src
        print('*'*20,i,'*'*20)
        print(dic)
        list.append(dic)

    # mycol.insert_many(list)
    if(i%50==0):time.sleep(600)
    # 下一页
    el=soup.find('a',{'class':'next'})
    driver.find_element_by_class_name('next').click()
    # driver.find_element_by_link_text(u"下一页").click()



time.sleep(5)
# driver.close()
