from selenium import webdriver
from bs4 import BeautifulSoup
import time


film_name_list_single_path='E:\\tjl\\其他\\crawler\\film_name_list_single.txt'
film_name_rating_nums='E:\\tjl\\其他\\crawler\\film_name_rating_nums.txt'
with open(film_name_list_single_path) as f:
    s=f.read()
tmp_list=s.split('\n')

driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)

driver.get("https://movie.douban.com/")
time.sleep(60)
driver.find_element_by_id("inp-query").click()
driver.find_element_by_id("inp-query").clear()

dic={}
for i,name in enumerate(tmp_list):
    print(i)
    driver.find_element_by_id("inp-query").click()
    driver.find_element_by_id("inp-query").clear()
    driver.find_element_by_id("inp-query").send_keys(name)
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='搜索：'])[1]/following::input[2]").click()
    soup = BeautifulSoup(driver.page_source)
    try:
        link_node = soup.find('span', class_="rating_nums")
        tmp = link_node.get_text()
        # tmp_list=tmp.split('\n')
        dic[name]=tmp
    except:
        print('评分没有找到，可能是暂无评分，用0分代替')
        dic[name] = 0

with open(film_name_rating_nums,'w') as f:
    f.write(str(dic))
    print('done')

time.sleep(1)
driver.close()