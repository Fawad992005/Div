class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
    def addbooks(self,book):
        self.books.append(book)
        self.nobooks = len(self.books)
    
    def showinfo(self):
        print(f"The Library has {self.nobooks} books.The books are:")
        for boo in self.books:
            print(boo)

obj = library()
while True:
    inpt = input("Enter the name of book to add in library, press 0 to exit: ")
    if inpt == "0":
        break
    obj.addbooks(inpt)
obj.showinfo()
while True:
    choose = input("Enter which book to choose or press 0 to exit: ")
    if choose in obj.books:
        print(f"{choose} is in the library")
    elif choose == "0":
        break
    else:
        print(f"{choose} is no in the library")
