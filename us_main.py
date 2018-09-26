import sqlite3
from sqlite3 import Error
class us_main():

    def __init__(self):
        super().__init__()
        self.create_DB()


    def create_DB(self):
        self.conn=sqlite3.connect("united_style.db")
        cur=self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS inventory(id integer PRIMARY KEY autoincrement, post_ID ,貨名, 類型, 顏色, 尺寸, 成本, 售價, link, Barcode, 日期, UNIQUE(post_ID,顏色,尺寸),FOREIGN KEY(post_ID,貨名) REFERENCES goods(post_ID,貨名))")
        cur.execute("CREATE TABLE IF NOT EXISTS in_DB(id integer PRIMARY KEY autoincrement, post_ID, 貨名, 顏色, 尺寸,庫存, 日期, FOREIGN KEY(post_ID,貨名) REFERENCES goods(post_ID,貨名) )")
        cur.execute("CREATE TABLE IF NOT EXISTS out_DB(id integer PRIMARY KEY autoincrement, 交收人員, Barcode, 日期)")
        cur.execute("CREATE TABLE IF NOT EXISTS people(id integer PRIMARY KEY autoincrement, 人名, 電話)")
        cur.execute("CREATE TABLE IF NOT EXISTS goods(post_ID,貨名,PRIMARY KEY(post_ID,貨名))")
        cur.execute("CREATE TABLE IF NOT EXISTS goods_amount(Barcode,Qty,PRIMARY KEY(Barcode))")
        #cur.execute("SELECT 庫存 from in_DB where 貨名=?",("a",))
        #temp=cur.fetchall()
        #for i in temp:
        #    print(i[0])
        #    print(type(i[0]))
        self.conn.commit()


    def add_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        conn.commit()

    def delete_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        conn.commit()

    def update_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        conn.commit()

    def search_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        return cur.fetchone()

    def search_items(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        return cur.fetchall()

    def search_all(self,conn,sql):
        cur=conn.cursor()
        cur.execute(sql)

        return cur.fetchall()






if __name__=="__main__":
    us_main()
