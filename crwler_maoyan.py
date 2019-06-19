from selenium import webdriver
from bs4 import BeautifulSoup
import re, time

driver = webdriver.Firefox()
driver.maximize_window()
# driver.minimize_window()
driver.implicitly_wait(30)

driver.get("https://piaofang.maoyan.com/?ver=normal")

i = 0
with open('ticket.txt','w') as f:
    while (True):
        if (i > 0): break
        i += 1
        time.sleep(1)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='明天'])[1]/following::span[1]").click()
        time.sleep(2)
        s = u"(.//*[normalize-space(text()) and normalize-space(.)='今天'])/preceding::span[" + str(i) + "]"
        el = driver.find_element_by_xpath(s)
        # 日期不存在，则继续找前一个
        while (el.text == ''):
            i += 1
            s = u"(.//*[normalize-space(text()) and normalize-space(.)='今天'])/preceding::span[" + str(i) + "]"
            el = driver.find_element_by_xpath(s)
        # print('日期：'+el.text)
        el.click()

        soup = BeautifulSoup(driver.page_source)
        link_node = soup.find('div', id=("ticket_tbody"))
        tmp = link_node.get_text()
        tmp_list=tmp.split('\n')
        print(tmp_list)
        n=int(len(tmp_list)/23)

        for j in range(n):
            dic = {}

            film_name=tmp_list[23*j+2]
            booking_office=tmp_list[23*j+3]
            actual_time_booking_office=tmp_list[23*j+6]
            booking_office_percent=tmp_list[23*j+8]
            chip_formatione_percent=tmp_list[23*j+10]
            attendance_rate=tmp_list[23*j+14]

            dic['film_name']=film_name
            dic['booking_office']=booking_office
            dic['actual_time_booking_office']=actual_time_booking_office
            dic['booking_office_percent']=booking_office_percent
            dic['chip_formatione_percent']=chip_formatione_percent
            dic['attendance_rate']=attendance_rate

            f.write(str(dic))
            f.write('\n')

f.close()
print('写文件完成')

time.sleep(5)
driver.close()
