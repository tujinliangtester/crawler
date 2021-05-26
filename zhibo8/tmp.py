import json
dicB=[]
with open('tmp.json', 'r', encoding='utf8') as f:
    content=f.read()
    contentJson=json.loads(content)
    for i in contentJson:
        item={}
        item['title']=i['title']

        tmpArray=[]
        content=i['content']
        for j in content:
            splited=str(j['text']).split(' ')
            tmpDicJ={}
            tmpDicJ['timeStr']=splited[0]
            tmpDicJ['matchName']=splited[1]
            tmpDicJ['teamA']=splited[2]
            tmpDicJ['teamB']=splited[4]
            tmpDicJ['imgs']=j['imgs']

            tmpArray.append(tmpDicJ)
        item['content']=tmpArray
        dicB.append(item)

print(dicB)
with open('./tmp2.json','w') as f:
    f.write(str(dicB))
