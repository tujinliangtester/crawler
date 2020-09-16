from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)

film_name='C:/tjl/临时/725d4a7401f69e3143329465.txt'

url='https://wenku.baidu.com/view/725d4a7401f69e3143329465.html'
driver.get(url)
time.sleep(10)
soup = BeautifulSoup(driver.page_source)

# link_nodes = soup.find('p', class_="reader-word-layer")
link_nodes = soup.findAll('p', class_="p-txt")
tmp=''
print(link_nodes)

for link_node in link_nodes:
    try:

        tmp += link_node.get_text()
    except  :
        print(link_node)
        print('e')
with open(film_name,'w',encoding='utf8') as f:
    f.write(tmp)
    print('done')
'''


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
'''
time.sleep(1)
driver.close()