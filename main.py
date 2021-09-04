from myDB import DBHelper


def main():
    db = DBHelper()
    list1 = list()
    list2 = list()
    list3 = list()
    while True:
        print('********************** WELCOME ****************************\n')
        print('Enter 1 for login')
        print('Enter 2 for register')
        try:
            choice = int(input('Enter your choice\n'))
            if choice == 1:
                print('********** LOGIN PAGE *************\n')
                username = input('Enter username :\n')
                password = input('Enter password :\n')
                a = db.login_admin(username, password)
                if a == True:
                    print('Login Successful\n')
                    ch = int(input('''Enter 1 for Repository
                                      2 for Invoice
                                      3 for Reports\n'''))
                    if ch == 1:  # Repository
                        ch1 = int(input('''Enter 1 for Customer
                                                 2 for Product
                                                 3 for Discount\n'''))
                    elif ch == 2:  # Invoice
                        ch1 = int(input('''Enter 1 for Upload Invoice 
                                                 2 for Delete Invoice\n'''))
                        if ch1 == 1:
                            print('******* UPLOAD INVOICE **********\n')
                            custID = input('Enter customer id available in the DB\n')
                            ch2 = int(input('''Enter 1 for Add Product
                                                     2 for Remove Product'''))
                            if ch2 == 1:
                                print('Available products')
                                db.fetch_all_product_data()
                                productID = input('Enter product id of the product you want to buy.')
                                quantity = int(input('Enter quantity. Min is 1 and max is 5'))
                                price = db.fetch_price_of_product(productID)
                                list1.append(productID)
                                list2.append(quantity)
                                list3.append(price)
                                while True:
                                    ch3 = input('Add another product? Y or N')
                                    if ch3 == 'N' or ch3 == 'n':
                                        break
                                    elif ch3 == 'Y' or ch3 == 'y':
                                        productID2 = input('Enter product id of the product you want to buy')
                                        quantity2 = int(input('Enter quantity. Min is 1 and max is 5'))
                                        price2 = db.fetch_price_of_product(productID2)
                                        list1.append(productID)
                                        list2.append(quantity2)
                                        list3.append(price2)

                    elif ch == 3:  # Reports
                        ch1 = int(input('''Enter 1 for Sales by Product
                                                 2 for Sales by Discount
                                                 3 for Sales by Location
                                                 4 for Sales by Customer Category
                                                 5 for Sales by Product Band

                                               '''))


                else:
                    print('Username or password is incorrect\n')
            elif choice == 2:
                print('************ REGISTER AS AN ADMIN ************************\n')
                fname = input('Enter your first name : \n')
                lname = input('Enter your last name : \n')
                dob = input('Enter your birthdate : \n')
                gender = input('Enter your gender : \n')
                contact = input('Enter your contact number : \n')
                id = int(input('Enter your id : \n'))
                password = input('Enter password : \n')
                email = input('Enter your email : \n')  # username
                db.register_admin(fname, lname, dob, gender, contact, id, password, email)
            else:
                print('Invalid Input')
        except Exception as e:
            print(e)
            print('Some exception occurred\n')


if __name__ == "__main__":
    main()
