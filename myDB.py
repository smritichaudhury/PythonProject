import datetime
import mysql.connector
import random


class DBHelper:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', port='3306', user='root', password='winteriscoming@98',
                                           database='training', auth_plugin='mysql_native_password')
        query1 = 'create table if not exists users(FirstName varchar(20),LastName varchar(30),DoB varchar(10),Gender varchar(' \
                 '10),' \
                 'ContactNumber varchar(10),UserId int primary key,password varchar(15),email varchar(30),category ' \
                 'varchar(10)) '
        query2 = "create table if not exists customer(customerID varchar(8) primary key,customerName varchar(30),customerCategory varchar(15),customerLocation varchar(20)," \
                 "contactNumber varchar(10))"
        query3 = "create table if not exists product(productID varchar(6) primary key,productName varchar(30),productCategory varchar(15),productBrand varchar(20)," \
                 "productDescription varchar(40),productPrice int, stock int)"
        query4 = "create table if not exists discount(discountID varchar(7) primary key,discountName varchar(30)," \
                 "discountDescription varchar(40),discountPrice int)"
        query5 = "create table if not exists invoice(invoiceID int primary key,invoiceDate varchar(20),customerID varchar(8),customerName varchar(30),productID varchar(6),paymentMode varchar(20),tax int,totalPrice int)"
        cursor = self.con.cursor()
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        cursor.execute(query4)
        cursor.execute(query5)
        print('Tables are created\n')

    # Insert data of admin
    def register_admin(self, fname, lname, dob, gender, contact, id, password, email):
        category = 'admin'
        query = 'insert into users(FirstName,LastName,DoB,Gender,ContactNumber,UserId,password,email,category) values("{}",' \
                '"{}","{}","{}","{}",{},"{}","{}","{}")'.format(fname, lname, dob, gender, contact, id, password,
                                                                email, category)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('Record has been inserted into my_users\n')

    # Login
    def login_admin(self, email, password):
        flag = False
        query1 = "select email,password from users where category='admin'"
        cursor = self.con.cursor()
        cursor.execute(query1)
        for row in cursor:
            if row[0] == email and row[1] == password:
                flag = True
            else:
                flag = False
        return flag

    def calculate_bill(self,list1,list2,list3):
        total_price = 0
        for i in range(0, len(list3)):
            total_price += list3[i]


    # Update invoice
    def update_invoice(self, custID, custName, ):
        invoice_id = random.sample(range(1, 100), 1)
        invoice_date = datetime.date.today()

    # Fetching all product data
    def fetch_all_product_data(self):
        query = "select * from product"
        cursor = self.con.cursor()
        cursor.execute(query)
        print('Fetching all data from table\n\n')
        for row in cursor:
            print('Product ID : ', row[0], )
            print('Product Name : ', row[1])
            print('Product Category : ', row[2])
            print('Product Description : ', row[3])
            print('Product Price : ', row[4])
            print('Quantity : ', row[5], '\n\n')

    def fetch_price_of_product(self, productID):
        query = "select productPrice from product where productID='{}'".format(productID)
        cursor = self.con.cursor()
        cursor.execute(query)
        for row in cursor:
            price = row[0]
        print(price)
        return price

    # delete user
    def delete_user(self, id):
        query = "delete from my_users where user_id ={}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('User {} has been deleted'.format(id), '\n')

    # update user
    def update_user(self, id, name, phone):
        query = "update my_users set user_name='{}',phone_number='{}' where user_id={}".format(name, phone, id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('User {} has been updated'.format(id), '\n')


DBHelper().fetch_price_of_product('PRD234')
