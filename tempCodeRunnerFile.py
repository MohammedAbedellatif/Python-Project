from Library import books, users

with open("books.txt", "wb") as foofile:
    val = foofile.read().decode("UTF-8")
    books.append(val)
    print(books[0])
with open("users.txt", "wb") as foofile:
    vall = foofile.read().decode("UTF-8")
    users.append(val)
    print(users[0])
