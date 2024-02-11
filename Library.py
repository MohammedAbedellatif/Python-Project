import os
import pickle

books = []
users = []


def main():
    global books
    global users
    print("***********")
    if os.path.getsize("books.txt") != 0:
        with open("books.txt", "rb") as booksFile:
            val = booksFile.read()
            data = pickle.loads(val, fix_imports=True, encoding='ASCII', errors='strict', buffers=None)
            books = data
    if os.path.getsize("users.txt") != 0:
        with open("users.txt", "rb") as usersFile:
            val = usersFile.read()
            data = pickle.loads(val, fix_imports=True, encoding='ASCII', errors='strict', buffers=None)
            users = data
    admin = Admin("REDA")

    while True:
        print("============ WELCOME TO OUR LIBRARY ============")
        print("Please choose an option to continue:\n1-Admin Login.\n2-User Login.\n3-EXIT.")
        ans = input("Choose(1,2,3): ")
        if ans == "1":
            loggedin = True
            if loggedin:
                print("Please,Enter name and password.")
                name = input("Username: ")
                password = input("Password: ")
                if name != "000" and password != "000":
                    loggedin = False
                    continue
            while True:
                print("===========================================")
                print("Please, select what do you want to do?:")
                print("1)Mange Books\n2)Mange Users\n3)CLOSE")
                soelected = int(input("Enter your choice: "))
                if soelected == 1:
                    print("Please, choose any one option:")
                    print("1-Add Book.\n2-Delete Book.\n3-Update Book.\n4-Search.\n5-Show Books."
                          "\n6-Show Issued Books.\n7-Return Book.\n8-Issue Book.\n9-Logout.")
                    # save changes
                    bookF = open('books.txt', 'wb')
                    pickle.dump(books, bookF)
                    bookF.close()
                    res = input("Enter your choice: ")
                    print("===========================================")
                    if res == "1":
                        name = input("Enter the book name: ")
                        while True:
                            isFound = False
                            id = input("Enter the book id: ")
                            for b in books:
                                if b.id == id:
                                    isFound = True
                                    break
                            if isFound:
                                print("This id already exist try again..")
                            else:
                                break
                        auther = input("Enter the book auther: ")
                        returnDate = input("Enter the return date: ")
                        price = input("Enter the price: ")
                        quantity = input("Enter the quantity: ")
                        rackNo = input("Enter the rack Number: ")
                        subject = input("Enter the subject: ")
                        admin.addBook(name, id, auther, returnDate, price, quantity, rackNo, subject)
                        print("The book added successfully ^_^")
                        continue
                    elif res == "2":
                        admin.showBooks()
                        id = input("Enter id that you want to delete: ")
                        b = admin.search(id)
                        if b:
                            admin.deleteBook(id)
                            print("The book was deleted successfully ^_^")
                        else:
                            print("This id not found!!")
                            continue
                    elif res == "3":
                        admin.showBooks()
                        id = input("Enter id that you want to update: ")
                        b = admin.search(id)
                        if b:
                            admin.updateBook(id)
                            print("The book was updated successfully ^_^")
                        else:
                            print("This id not found!!")
                            continue
                    elif res == "4":
                        id = input("Enter id that you want to search: ")
                        b = admin.search(id)
                        if b:
                            print("This book is found ^_^")
                            isAvailable = "Available"
                            if b.avilableBooks == 0:
                                isAvailable = "Not Available"
                                print("Name: " + b.name, "\nid: ", b.id, "\nstate: " + isAvailable)
                        else:
                            print("This book not found!!")
                            continue
                    elif res == "5":
                        admin.showBooks()
                        continue
                    elif res == "6":
                        admin.showIssue()
                        continue
                    elif res == "7":
                        id = input("Enter id that you want to return: ")
                        # admin.showBooks()
                        b = admin.search(id)
                        if b:
                            admin.returnBook(id)
                            print("The book was returned successfully ^_^")
                        else:
                            print("This id not found!!")
                            continue
                    elif res == "8":
                        print("========================================")
                        admin.displayUsers()
                        admin.showBooks()
                        print("========================================")
                        bookId = input("Enter the book id:")
                        userId = input("Enter the user id:")
                        admin.assuBook(bookId, userId)
                        continue
                    elif res == "9":
                        print("Admin logged out..")
                        break
                    else:
                        print("Invalid input try again..")
                if soelected == 2:
                    print("1-Add User.\n2-Display Users.\n3-Update User.\n4-Delete User.\n5-Logout.")
                    userF = open('users.txt', 'wb')
                    pickle.dump(users, userF)
                    userF.close()
                    ress = input("Enter your choice: ")
                    print("===========================================")
                    if ress == "1":
                        while True:
                            isFound = False
                            id = input("Enter the User Id: ")
                            for u in users:
                                if u.id == id:
                                    isFound = True
                                    break
                            if isFound:
                                print("This id already exist try again..")
                            else:
                                break
                        name = input("Enter the user name: ")
                        address = input("Enter the user address: ")
                        admin.addUser(id, name, address)
                        print("The user added successfully ^_^")
                        continue
                    elif ress == "2":
                        admin.displayUsers()
                        continue
                    elif ress == "3":
                        admin.displayUsers()
                        id = input("Enter id that you want to update: ")
                        user = admin.searchUser(id)
                        if user:
                            admin.updateBook(id)
                            print("The user was updated successfully ^_^")
                        else:
                            print("This id not found!!")
                            continue
                    elif ress == "4":
                        admin.displayUsers()
                        id = input("Enter id that you want to delete: ")
                        user = admin.searchUser(id)
                        if user:
                            admin.deleteUser(id)
                            print("The user was deleted successfully ^_^")
                        else:
                            print("This id not found!!")
                            continue
                    elif ress == "5":
                        print("Admin logged out..")
                        break
                    else:
                        print("Invalid input try again..")
                elif soelected == 3:
                    print("Admin logged out..")
                    break
        elif ans == "2":
            while True:
                print("===========================================")
                print("Please, select what do you want to do?:")
                print("1-Login by exist account.\n2-Create new account.\n3-EXIT.")
                rest = input("Enter your choice: ")
                print("===========================================")
                if rest == "1":
                    id = input("Enter your id: ")
                    user = None
                    for u in users:
                        if u.id == id:
                            user = u
                            break
                    if user:
                        print("===========================================")
                        print("Your account was logged in successfully ^_^")
                        while True:
                            print("1-View Issued Books.\n2-Search.\n3-View Available Books.\n4-Logout.")
                            res2 = input("Enter your choice: ")
                            if res2 == "1":
                                user.viewAssuedBooks()
                                continue
                            elif res2 == "2":
                                id = input("Enter book id: ")
                                user.search(id)
                                continue
                            elif res2 == "3":
                                user.viewAvailableBooks()
                                continue
                            else:
                                print("Your account was Logged out..")
                                break
                    else:
                        print("This id is not found try again..")
                elif rest == "2":
                    name = input("Enter Your name: ")
                    id = input("Enter Your id: ")
                    address = input("Enter Your address: ")
                    idIsFound = False
                    for u in users:
                        if u.id == id:
                            idIsFound = True
                            break
                    if idIsFound:
                        print("This id is already exist, try to login..")
                    else:
                        user = User(id, name, address)
                        admin.addUserAsObject(user)
                        print("===========================================")
                        print("your account created successfully ^_^")
                        # save changes
                        userF = open('users.txt', 'wb')
                        pickle.dump(users, userF)
                        userF.close()
                        while True:
                            print("1-View Issued Books.\n2-Search.\n3-View Available Books.\n4-Logout.")
                            res2 = input("Enter your choice: ")
                            if res2 == "1":
                                user.viewAssuedBooks()
                                continue
                            elif res2 == "2":
                                id = input("Enter book id: ")
                                user.search(id)
                                continue
                            elif res2 == "3":
                                user.viewAvailableBooks()
                                continue
                            else:
                                print("Your account was logged out..")
                                break
                else:
                    break
        elif ans == "3":
            print("Thank you ^_^")
            print("===========================================")
            break
        else:
            print("Invalid input try again..")


class User:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.assuedBooks = []

    def search(self, id):
        isFound = False
        b = None
        for book in books:
            if book.id == id:
                isFound = True
                b = book
                break

        if isFound:
            print("This book is found:")
            isAvailable = "Available"
            if b.avilableBooks == 0:
                isAvailable = "Not Available"
            print("Name: " + b.name, "\nid: ", b.id, "\nstate: " + isAvailable)
            print("**********")

        else:
            print("This book is not found!!")

    def viewAssuedBooks(self):
        print("=====================Issued Books:=====================")
        if len(self.assuedBooks) > 0:
            for b in self.assuedBooks:
                print("Name: " + b.name, "\nid: ", b.id)
                print("**********")
        else:
            print("No assued books")

    def viewAvailableBooks(self):
        print("=====================Available Books:=====================")

        for b in books:
            if b.avilableBooks > 0:
                print("Name: " + b.name, "\nid: ", b.id)
                print("**********")


class Book:

    def __init__(self, name, id, auther, returnDate, price, quantity, rackNo, subject):
        self.name = name
        self.id = id
        self.auther = auther
        self.returnDate = returnDate
        self.price = price
        self.quantity = int(quantity)
        self.rackNo = rackNo
        self.subject = subject
        self.avilableBooks = int(quantity)
        self.assuedBooks = 0

    def updateQuantity(self, value):
        newValue = int(value)
        self.quantity = newValue
        avilable = newValue - int(self.assuedBooks)
        self.avilableBooks = avilable


class Admin:
    def __init__(self, name):
        self.name = name

    def assuBook(self, bookId, userId):
        book = None
        user = None
        done = True
        for b in books:
            if b.id == bookId:
                book = b
                break

        for u in users:
            if u.id == userId:
                user = u
                break

        if (user == None):
            print("This user not found!!")
            done = False
        if (book == None):
            print("This book not found!!")
            done = False

        if done:
            if (book.avilableBooks > 0):
                user.assuedBooks.append(book)
                book.avilableBooks -= 1
                book.assuedBooks += 1
                print("The book issued successfully ^_^")
            else:
                print("This book is unavailable!!")

    def addBook(self, name, id, auther, returnDate, price, quantity, rackNo, subject):
        b = Book(name, id, auther, returnDate, price, quantity, rackNo, subject)
        books.append(b)

    def deleteBook(self, id):
        for b in books:
            if (b.id == id):
                books.remove(b)
                break

    def updateBook(self, id):
        for b in books:
            if b.id == id:
                name = input("Enter the new name: ")
                b.name = name

                auther = input("Enter the new auther: ")
                b.auther = auther

                returnDate = input("Enter the new returnDate: ")
                b.returnDate = returnDate

                price = input("Enter the new price: ")
                b.price = price

                quantity = input("Enter the new quantity: ")
                b.updateQuantity(quantity)

                rackNo = input("Enter the new rackNo: ")
                b.rackNo = rackNo

                subject = input("Enter the new subject: ")
                b.subject = subject
                break

    def search(self, id):
        for b in books:
            if b.id == id:
                return b

        return None

    def showBooks(self):

        print("=====================Books:=====================")
        for b in books:

            isAvailable = "Available"
            if b.avilableBooks == 0:
                isAvailable = "Not Available"
            print("Name: " + b.name, "\nid: ", b.id, "\nstate: " + isAvailable)
            print("****************")

    def showIssue(self):
        print("=====================Issued Books:=====================")
        for b in books:
            if b.assuedBooks > 0:
                print("Name: " + b.name, "\nid: ", b.id)
                print("****************")

    def returnBook(self, id):
        book = None
        for b in books:
            if b.id == id:
                book = b
                break
        for u in users:
            if b in u.assuedBooks:
                u.assuedBooks.remove(b)
                b.avilableBooks += 1
                b.assuedBooks -= 1

    def addUser(self, id, name, address):
        newUser = User(id, name, address)
        users.append(newUser)

    def addUserAsObject(self, user):
        users.append(user)

    def displayUsers(self):
        print("=====================Users:=====================")
        for user in users:
            print("Name: " + user.name, "\nid: ", user.id + "\naddress: " + user.address)
            print("****************")

    def deleteUser(self, id):
        for user in users:
            if user.id == id:
                users.remove(user)
                break

    def updateUser(self, id):
        for user in users:
            if user.id == id:
                name = input("Enter the new name: ")
                user.name = name

                address = input("Enter the new address: ")
                user.address = address
                break

    def searchUser(self, id):
        u = None
        for user in users:
            if user.id == id:
                u = user
                break

        return u


main()
