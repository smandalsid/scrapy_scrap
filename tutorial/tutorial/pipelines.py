# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import sqlite3
# import mysql.connector
import pymongo

class TutorialPipeline:

    # def __init__(self):
    #     self.create_conn()
    #     self.create_table()

    # def create_conn(self):
    #     # self.conn = sqlite3.connect("myquotes.db")
    #     self.conn = mysql.connector.connect(host="localhost", user="root", passwd="chunnu", database="quotes_db")
    #     self.cur = self.conn.cursor()

    # def create_table(self):
    #     self.cur.execute("""
    #         drop table if exists quotes
    #     """)
    #     self.cur.execute("""
    #         create table quotes(title varchar(100), author varchar(100), tag varchar(200))
    #     """)

    # def process_item(self, item, spider):
    #     self.store_db(item);
    #     print("Pipeline: "+item['title'][0])
    #     return item

    # def store_db(self, item):
    #     self.cur.execute("""
    #         insert into quotes values(%s, %s, %s)""",(
    #             item["title"][0],
    #             item["author"][0],
    #             item["tags"][0],
    #         ))
    #     self.conn.commit()

    def __init__(self):
        self.conn=pymongo.MongoClient("localhost", 27017)
        db=self.conn["quotes_db"]
        self.collection = db["quotes"]

    def process_item(self, item, spider):
        print(dict(item))
        self.collection.insert_one(dict(item))
        return item