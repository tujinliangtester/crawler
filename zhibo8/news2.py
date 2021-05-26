from selenium import webdriver
from bs4 import BeautifulSoup
import re, time
import requests
import csv
from util.elementXpathRelation import XpathRelation as xp

xp=xp()

driver = webdriver.Chrome()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)
base_url='https://www.zhibo8.cc'
driver.get(base_url)
time.sleep(5)

els=driver.find_elements_by_xpath(xp.findText('a','电竞'))
els[1].click()
time.sleep(1)

titles=driver.find_elements_by_xpath('//div[@class="box"]/div[@class="titlebar"]')
targetList=[]
for (i,title) in enumerate(titles):
    if(i==16):
        break
    print('\r','第{}次循环'.format(i),end='',flush=True)
    tmp='(//div[@class="box"])[{}]/div[@class="content"]//li'.format(i+1)
    contents = driver.find_elements_by_xpath(tmp)
    cs=[]
    for (j,c) in enumerate(contents):
        tmpC={}
        if(str(c.get_attribute('style')).find('display: none')>-1):
            continue
        tmpC['text']=c.text

        imgs=driver.find_elements_by_xpath(tmp+'[{}]//img'.format(j+1))
        imgUrlList=[]
        for img in imgs:
            imgUrlList.append(img.get_attribute('src'))
        tmpC['imgs']=imgUrlList
        cs.append(tmpC)

    targetItem={}
    targetItem['title']=title.text
    targetItem['content']=cs
    targetList.append(targetItem)
driver.close()
print(targetList)
import  json
with open('tmp.json', 'w', encoding='utf8') as f:
    f.write('[')
    for i in targetList:
        f.write(json.dumps(i).encode('gbk').decode('unicode_escape'))
        f.write(',')
    f.write(']')


