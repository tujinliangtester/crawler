from selenium import webdriver

browser = webdriver.Firefox()
browser.minimize_window()
browser.get("https://piaofang.maoyan.com/?ver=normal")
print(browser.page_source)
with open('res.html','w',encoding='utf-8') as f:
    f.write(browser.page_source)

browser.close()



