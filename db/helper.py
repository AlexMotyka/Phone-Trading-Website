import psycopg2
import datetime
from psycopg2.extras import RealDictCursor


class Connection:
    def __init__(self):
        con = psycopg2.connect(database='hermes', user='django', host='localhost', password='hermes')
        self.cur = con.cursor()
        self.dict = con.cursor(cursor_factory = RealDictCursor)
        self.commit = con.commit
        self.roll = con.rollback

    def get_models(self):
        self.cur.execute('select Distinct "MODEL","MODEL" from products ')
        return self.cur.fetchall()

    def get_memory(self):
        self.cur.execute('select distinct "MEMORY","MEMORY" from products where "MEMORY" is NOT NULL')
        return self.cur.fetchall()

    def most_sold24(self):
        now = datetime.datetime.today()
        #dayy = psycopg2.sql.Literal("day")
        self.cur.execute('select "MODEL" from products where extract(day from "DATE_POSTED") = %s;',(now,))
        return self.cur.fetchall()

    def phones_lta(self):
        self.cur.execute('select products."MODEL",products."PRICE",products."URL" '
                         'from products '
                         'INNER JOIN (select "MODEL", avg("PRICE") as "PRICE" '
                                    'from products '
                                    'group by "MODEL") as phoneav '
                         'on products."MODEL"=phoneav."MODEL"'
                         'where products."PRICE"< phoneav."PRICE"')
        return self.cur.fetchall()
    def bestdeal(self):
        self.cur.execute('select products."MODEL",products."PRICE",products."URL",(products."PRICE"-phoneav."PRICE") as dif '
                         'from products '
                         'INNER JOIN (select "MODEL", avg("PRICE") as "PRICE" '
                                    'from products '
                                    'group by "MODEL") as phoneav '
                         'on products."MODEL"=phoneav."MODEL"'
                         'where products."PRICE"< phoneav."PRICE"'
                         'order by dif')
        return self.cur.fetchall()

    def allproducts(self):
        self.cur.execute('select "ITEM_ID","PLATFORM","CARRIER", "MODEL", "MEMORY","PRICE","TITLE","URL" from products order by "DATE_POSTED"')
        return self.cur.fetchall()


    def get_phones(self,model_type,memory):
        self.dict.execute('select "ITEM_ID","PLATFORM","CARRIER", "MODEL", "MEMORY","PRICE","TITLE","URL" from products where "MODEL"=%s and "MEMORY"=%s', [model_type,memory])
        return self.dict.fetchall()

    def get_users(self):
        self.cur.execute('select "NAME", "EMAIL" from customers')
        return self.cur.fetchall()


    def cust_buy(self,item_id,amount,cust_id):
        sql = 'insert into purchases ("PURCHASE_AMOUNT","DATE_BOUGHT","CUST_ID","ITEM_ID") values (%s,current_timestamp,%s,%s)'
        try:
            self.cur.execute(sql,[amount,cust_id,item_id])
            self.commit()
            print("Success")
        except:
            self.roll()
            print("Failure")


    def cust_sell(self,item_id,amount,cust_id):
        sql = 'update purchases set "SALE_AMOUNT"= %s, "DATE_SOLD"=current_timestamp where "CUST_ID"=%s and "ITEM_ID"=%s'
        try:
            self.cur.execute(sql,[amount,cust_id,item_id])
            self.commit()
            print("Success")
        except:
            self.roll()
            print("Failure")

    def get_active_users(self):
        self.cur.execute('select "NAME","EMAIL" '
                         'from customers, purchases '
                         'where purchases."CUST_ID" = customers."CUST_ID"')
        return self.cur.fetchall()

    def users_trans(self,email):
        self.cur.execute('select "SALE_AMOUNT","DATE_SOLD","PURCHASE_AMOUNT","DATE_BOUGHT","SHIPPING","NAME" '
                         'from customers, purchases '
                         'where purchases."CUST_ID"=customers."CUST_ID" and purchases."CUST_ID"= ( '
                            'select "CUST_ID" '
                            'from customers  '
                            'where "EMAIL" = %s)',[email])
        return self.cur.fetchall()
    def biggest_gains(self):
        self.cur.execute('select "CUST_ID","ITEM_ID",("SALE_AMOUNT"-"PURCHASE_AMOUNT") as profit '
                         'from purchases '
                         'where "SALE_AMOUNT" is NOT NULL '
                         'order by profit DESC ')
        return self.cur.fetchall()

    def weakly_returns(self):
        self.cur.execute('select purchases."ITEM_ID" '
                         'from purchases '
                         'INNER JOIN (select "ITEM_ID",("SALE_AMOUNT"-"PURCHASE_AMOUNT")/(extract(minute from "DATE_SOLD"-"DATE_BOUGHT")/(60*24*7)) as gain '
                            'from purchases order by gain DESC) as hot '
                         'ON purchases."ITEM_ID"=hot."ITEM_ID" '
                         'ORDER by hot.gain DESC')
        return self.cur.fetchall()
