import json
dicB=[]
with open('./news.json','r') as f:
    content=f.read()
    contentJson=json.loads(content)
    for i in contentJson:
        item={}
        item['title']=i['title']

        tmpArray=[]
        content=i['content']
        for j in content:
            splited=str(j).split(' ')
            tmpArray.append(splited)