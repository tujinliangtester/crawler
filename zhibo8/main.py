from selenium import webdriver
from bs4 import BeautifulSoup
import re, time
import requests
import csv
driver = webdriver.Firefox()
driver.minimize_window()
# driver.minimize_window()
driver.implicitly_wait(30)
driver.get("https://www.zhibo8.cc/zuqiu/index_old.htm")
time.sleep(1)
base_url='https://www.zhibo8.cc'

target_str_list=['中国','国足']

soup = BeautifulSoup(driver.page_source)
link_nodes = soup.find_all('a')
els=driver.find_elements_by_tag_name('a')
with open('test.csv','w')as f:
    f_csv = csv.writer(f)
    for (i,link_node) in enumerate(link_nodes) :
        try:
            tmp_text=link_node.get_text()
            for target_str in target_str_list:
                if(tmp_text.find(target_str)==-1):
                    continue
                driver2 = webdriver.Firefox()
                driver2.minimize_window()
                driver2.get(base_url+link_node['href'])
                time.sleep(3)
                soup_hot = BeautifulSoup(driver2.page_source)
                link_nodes_hot=soup_hot.find_all('div','case')
                for link_node_hot in link_nodes_hot:
                    tmp_row=[tmp_text,link_node_hot.text]
                    f_csv.writerow(tmp_row)
                driver2.close()
                break
        except Exception:
            print(Exception)
        if (i > 20000): break
driver.close()
