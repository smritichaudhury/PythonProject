from myDB import DBHelper


def main():
    db = DBHelper()
    list1 = list()  # product id
    list2 = list()  # qty
    list3 = list()  # price
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
                if a == 'Login Successful':
                    print('Login Successful\n')
                    try:
                        while True:
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
                                        while True:
                                            productID = input('Enter product id of the product you want to buy.\n')
                                            quantity = int(input('Enter quantity. Min is 1 and max is 5.\n'))
                                            price = db.fetch_price_of_product(productID)
                                            list1.append(productID)
                                            list2.append(quantity)
                                            list3.append(price)
                                            total = db.calculate_bill(list3)
                                            ch3 = input('Do you want to select payment mode? Y or N\n')
                                            if ch3 == 'Y' or ch3 == 'y':
                                                break
                                        paymentMode = input('''Enter payment mode. 
                                                 Select 1 for GPay
                                                 2 for Paytm
                                                 3 for Credit/Debit
                                                 4 for UPI\n''')
                                        if paymentMode == 1:
                                            payment = 'GPay'
                                        elif paymentMode == 2:
                                            payment = 'PayTM'
                                        elif paymentMode == 3:
                                            payment = 'Credit/Debit'
                                        else:
                                            payment = 'UPI'
                                        db.update_invoice(custID, total, list1, list2, quantity, list3, payment)
                                elif ch == 2:
                                    print('*************** DELETE INVOICE ********************')
                                    db.fetch_all_invoice_data()
                                    while True:
                                        deleteInvoice = input('Enter the invoice id to delete\n')
                                        ch3 = input('Are you sure ? Y or N\n')
                                        if ch3 == 'Y' or 'y':
                                            db.delete_invoice_by_id(deleteInvoice)
                                            break
                                        elif ch3 == 'N' or 'n':
                                            print('Invoice deletion cancelled.\n')
                                            break
                            elif ch == 3:  # Reports
                                ch1 = int(input('''Enter 1 for Sales by Product
                                           2 for Sales by Discount
                                           3 for Sales by Location
                                           4 for Sales by Customer Category
                                           5 for Sales by Product Band
                                               \n'''))

                            elif ch > 3:
                                print('Enter number from 1-3.\n\n')

                    except ValueError:
                        print('Invalid input.Only integer is allowed.\n')
                else:
                    print(a, 'Enter again.\n')
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
            print('Only numeric values are allowed\n')


if __name__ == "__main__":
    main()
