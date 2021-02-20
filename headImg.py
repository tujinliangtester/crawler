from urllib import request

url = "http://headimgqn.szysx8.cn/1030.jpg"
request.urlretrieve(url,'1')

for i in range(2000,3000):
    url = "http://headimgqn.szysx8.cn/{}.jpg".format(i)
    name='{}.jpg'.format(i)
    try:
        request.urlretrieve(url,name)
    except:
        print('err')
