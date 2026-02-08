# Using Inheritance OOP for LMS


class Book:
     def __init__(self, name, author):
          self.name = name
          self.author = author
          self.available = True

     def show(self):
          status = "Available" if self.available else "Borrowed"
          print(self.name, "-", self.author, "-", status)

class EBook(Book):
     def __init__(self, name, author, size):
          super().__init__(name, author)   
          self.size = size

     def show(self):
          status = "Available" if self.available else "Borrowed"
          print(self.name, "-", self.author, "-", self.size, "-", status)

class Library:
     def __init__(self):
          self.books = []

     def add_book(self):
          print("\n1. Physical Book")
          print("2. EBook")
          choice = input("Choose book type: ")

          name = input("Enter book name: ")
          author = input("Enter author name: ")

          if choice == "1":
               book = Book(name, author)
          elif choice == "2":
               size = input("Enter ebook size: ")
               book = EBook(name, author, size)
          else:
               print("Invalid choice.")
               return

          self.books.append(book)
          print("Book added successfully!")

     def show_books(self):
          if not self.books:
               print("No books available.")
               return

          for book in self.books:
               book.show()   # POLYMORPHISM (important)

     def borrow_book(self):
          name = input("Enter book name to borrow: ")
          for book in self.books:
               if book.name == name:
                    if book.available:
                         book.available = False
                         print("Book borrowed!")
                    else:
                         print("Book already borrowed.")
                    return
          print("Book not found.")

     def return_book(self):
          name = input("Enter book name to return: ")
          for book in self.books:
               if book.name == name:
                    if not book.available:
                         book.available = True
                         print("Book returned!")
                    else:
                         print("This book was not borrowed.")
                    return
          print("Book not found.")


library = Library()

while True:
     print("\n Library Menu ")
     print("1. Add Book")
     print("2. Show Books")
     print("3. Borrow Book")
     print("4. Return Book")
     print("5. Exit")

     choice = input("Choose an option: ")

     if choice == "1":
          library.add_book()
     elif choice == "2":
          library.show_books()
     elif choice == "3":
          library.borrow_book()
     elif choice == "4":
          library.return_book()
     elif choice == "5":
          print("EXiTED")
          break
     else:
          print("Invalid choice.")
