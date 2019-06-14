from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)

driver.get("https://piaofang.maoyan.com/?ver=normal")
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='明天'])[1]/following::span[1]").click()
#todo 需要对不同的日期、月份进行处理
driver.find_element_by_xpath(
    u"(.//*[normalize-space(text()) and normalize-space(.)='儿童节'])[1]/following::span[4]").click()

soup=BeautifulSoup(driver.page_source)
# print("正则表达式匹配")
link_node = soup.find('div',id=("ticket_tbody"))
print(link_node.get_text())
# todo 需要进一步将获得的数据进行整理，保存，以便后续使用