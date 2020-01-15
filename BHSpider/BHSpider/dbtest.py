import mysql.connector
import json
import codecs
import logging
import requests 
item= {'novel_Author': '雨水都没有',
 'novel_CoverURL': 'https://image.baihexs.com/67/67939/67939s.jpg',
 'novel_ID': '67939',
 'novel_Intro': '肆意挥洒激情的游戏人生，打破现实框架的无尽幻想！',
 'novel_Isfinished': '连载中',
 'novel_LatestUpdateTime': '2019-03-10',
 'novel_Name': '安玄界之神级天赋',
 'novel_Type': '其他类型',
 'novel_Url': 'https://www.baihexs.com/book/67939.html',
 'novel_Wordscount': 289000}  
conn = mysql.connector.connect(user='root',
                                       password='123456',
                                       database='novel',
                                       host='10.60.2.175',port=3306,charset='utf8')
cursor = conn.cursor()
try:
            print('item=',item)
            sql="insert into novels( novel_Url , novel_ID , novel_Author , novel_Name , novel_CoverURL , novel_Intro , novel_Type , novel_Isfinished , novel_Wordscount , novel_LatestUpdateTime) values ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
            params = (item["novel_Url"], item["novel_ID"], item["novel_Author"], item["novel_Name"], item["novel_CoverURL"],item["novel_Intro"], item["novel_Type"], item["novel_Isfinished"],item["novel_Wordscount"], item["novel_LatestUpdateTime"])
            insert = cursor.execute(sql, params)
            conn.commit()
except Exception as e:
            print('--------------database operation exception!!-----------------')
            print(e)
            conn.rollback()
finally:
            cursor.close()
            conn.close()
