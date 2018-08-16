import sqlite3

class us_main():

    def __init__(self):
        super().__init__()
        self.create_DB()


    def create_DB(self):
        self.conn=sqlite3.connect("united_style.db")
        cur=self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS inventory(id integer PRIMARY KEY autoincrement, post_ID ,貨名, 類型, 顏色, 尺寸, 成本, 售價, link, Barcode, 日期)")
        cur.execute("CREATE TABLE IF NOT EXISTS in_DB(id integer PRIMARY KEY autoincrement, post_ID, 貨名, 顏色, 尺寸,庫存, 日期 )")
        cur.execute("CREATE TABLE IF NOT EXISTS out_DB(id integer PRIMARY KEY autoincrement, 交收人員, Barcode, 日期)")
        cur.execute("CREATE TABLE IF NOT EXISTS people(id integer PRIMARY KEY autoincrement, 人名, 電話)")
        self.conn.commit()


    def add_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        conn.commit()

    def delete_item(self,conn,sql,value):
        cur=conn.cursor()
        cur.execute(sql,value)
        conn.commit()


    def search_item(self,conn,sql):
        pass







if __name__=="__main__":
    us_main()
