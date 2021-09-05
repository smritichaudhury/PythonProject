import datetime
import mysql.connector


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
        query5 = "create table if not exists invoice(invoiceID int primary key NOT NULL AUTO_INCREMENT,invoiceDate varchar(20),customerID varchar(8),customerName varchar(30),productID varchar(6),paymentMode varchar(20),tax int,totalPrice int)"
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
        flag = ''
        query1 = "select email,password from users where category='admin'"
        cursor = self.con.cursor()
        cursor.execute(query1)
        for row in cursor:
            if row[0] == email:
                if row[1] == password:
                    flag = 'Login Successful'
                else:
                    flag = 'Incorrect password'
            else:
                flag = 'Incorrect username'
        return flag

    def calculate_bill(self, list3):
        total_price = 0
        for i in range(0, len(list3)):
            total_price += list3[i]
        return total_price

    # Update invoice
    def update_invoice(self, custID, total, list1, list2, quantity, list3, payment):
        invoice_date = datetime.date.today()
        query1 = "select customerName from customer where customerID='{}'".format(custID)
        cursor = self.con.cursor()
        cursor.execute(query1)
        tax = total + 10
        for i in cursor:
            custName = i[0]
        for i in range(len(list1)):
            productID = list1[i]
            query2 = "insert into invoice(invoiceDate,customerID,customerName,productID,paymentMode,tax,totalPrice)" \
                     "values('{}','{}','{}','{}','{}',{},{})".format(invoice_date, custID, custName,
                                                                     productID, payment, tax, total)
            cursor.execute(query2)
        self.con.commit()
        print('Invoice has been added\n')

    def fetch_all_invoice_data(self):
        query = "select * from invoice"
        cursor = self.con.cursor()
        cursor.execute(query)
        print('Fetching all data from invoice\n\n')
        for row in cursor:
            print('Invoice ID : ', row[0], )
            print('Invoice Date : ', row[1])
            print('Customer ID : ', row[2])
            print('Customer Name : ', row[3])
            print('Product ID : ', row[4])
            print('Payment Mode : ', row[5])
            print('Tax : ', row[5])
            print('Total Price : ', row[5], '\n\n')

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

    # delete invoice
    def delete_invoice_by_id(self, id):
        query = "delete from invoice where invoiceID ={}".format(id)
        cursor = self.con.cursor()
        cursor.execute(query)
        self.con.commit()
        print('Invoice {} has been deleted'.format(id), '\n')


