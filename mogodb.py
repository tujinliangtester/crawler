import pymongo


def my_study():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # dblist = myclient.list_database_names()
    # print(dblist)
    mydb = myclient["NationalDayOnWeiBo"]

    # MongoDB 使用数据库对象来创建集合
    mycol = mydb["NationalDayOnWeiBoSet"]

    collist = mydb.list_collection_names()
    print(collist)
    # collist = mydb.collection_names()
    if "NationalDayOnWeiBoSet" in collist:  # 判断 sites 集合是否存在
        print("集合已存在！")

    # mydict = { "nickname": "无锡都市生活广播", "feed_list_content": "【今日提醒】转眼已到九月底，后天起就是"}
    #
    # x=mycol.insert_one(mydict)
    # print(x)

    # x=mycol.find_one()
    # print(x)

    pipeline = [
        {"$group": {"_id": "$feed_list_content", "count": {"$sum": 1}}},
        {"$match": {'_id': {"$regex": ".*我和我的祖国.*"}}}
    ]
    x = mycol.aggregate(pipeline)
    list_x = list(x)
    print('我和我的祖国', len(list_x))
    for item in list_x:
        print(item)

    pipeline = [
        {"$group": {"_id": "$feed_list_content", "count": {"$sum": 1}}},
        {"$match": {'_id': {"$regex": ".*女排.*"}}}
    ]
    x = mycol.aggregate(pipeline)
    list_x = list(x)
    print('女排', len(list_x))
    for item in list_x:
        print(item)

    pipeline = [
        {"$group": {"_id": "$feed_list_content", "count": {"$sum": 1}}},
        {"$match": {'_id': {"$regex": ".*郎平.*"}}}
    ]
    x = mycol.aggregate(pipeline)
    list_x = list(x)
    print(len(list_x))
    for item in list_x:
        print(item)


if __name__ == '__main__':
    my_study()
