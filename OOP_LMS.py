# Library Management System
# Add book, remove book, search book, display books
# We will be using OOP for this task


class Book:
     def __init__(self, name, author, pages, price):
          self.name = name
          self.author = author
          self.pages = pages
          self.price = price
 
class Ebook(Book):
     def __init__(self,  name, author, pages, price, size):
          super().__init__(name, author, pages, price)
          self.size = size
 
class LMS:
     books = []
    # books will append the book object
    
     def add_book(self, book):
        # To add a book, we receive the book object and append it to the books list
        self.books.append(book)
    
     def display_book(self):
        # If the object is Ebook => display size
        # else: display Physical Book
        for book in self.books:
            print(f"Name = {book.name}")
            print(f"Author = {book.author}")
            print(f"Pages = {book.pages}")
            print(f"Price = {book.price}")
            if "Ebook" in str(book):
                print(F"Size = {book.size}")
            # else:
            #     # print("This is a Physical Book")
            #     pass
            print()
            
    
     def search_book(self):
        book_name = input("Enter book name to search: ")
        books = self.books
        for book in self.books:
            if book.name == book_name:
                index = self.books.index(book)
                print(f"Book found at index {index}")
                break
        else:
            print(f"{book_name} not found")
            
    
     def remove_book(self):
        book_name = input("Enter book name to remove: ")
        books = self.books
        for book in self.books:
            if book.name == book_name:
                # index = self.books.index(book)
                self.books.remove(book)
                print("Book Removed")
                self.display_book()
                break
        else:
            print(f"{book_name} not found")
    
    
b1 = Book("Lectures on the History of Philosophy", "HardPress, Hegel Georg Wilhelm Friedric", 518, 250)
b2 = Book("Summary Record of the Meeting", "Ujjwal Neupane", 200, 150)
b3 = Book("Parijaat", "Jhamak Kumari Ghimire", 628, 500)
eb1 = Ebook("Alex Cross","Ram Sharma",450,100,"10MB")
eb2 = Ebook("MunaMadan","Laxmi Prasad Devkota",300,200,"8MB")
eb3 = Ebook("ABC","ABC",450,100,"10MB")

lms1 = LMS()
lms1.add_book(b1)
lms1.add_book(b2)
lms1.add_book(b3)
lms1.add_book(eb1)
lms1.add_book(eb2)
lms1.add_book(eb3)

# lms1.display_book()

lms1.search_book()

# lms1.remove_book()
