# -------- Book Class --------
class Book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"{self.book_id} | {self.name} | {self.author} | {status}")


# -------- Library Class --------
class Library:
     def __init__(self):
          self.books = []

     def add_book(self):
          book_id = input("Enter Book ID: ")
          name = input("Enter Book Name: ")
          author = input("Enter Author Name: ")
          book = Book(book_id, name, author)
          self.books.append(book)
          print("Book added successfully!")

     def display_books(self):
          if not self.books:
               print("No books available.")
               return

          print("\nID | Name | Author | Status")
          print("-" * 30)
          for book in self.books:
               book.display()

     def search_book(self):
          book_id = input("Enter Book ID to search: ")
          for book in self.books:
               if book.book_id == book_id:
                    print("Book found:")
                    book.display()
                    return
          print("Book not found.")

     def borrow_book(self):
          book_id = input("Enter Book ID to borrow: ")
          for book in self.books:
               if book.book_id == book_id:
                    if book.available:
                         book.available = False
                         print("Book borrowed successfully!")
                    else:
                         print("Book already borrowed.")
                    return
          print("Book not found.")

     def return_book(self):
          book_id = input("Enter Book ID to return: ")
          for book in self.books:
               if book.book_id == book_id:
                    if not book.available:
                         book.available = True
                         print("Book returned successfully!")
                    else:
                         print("This book was not borrowed.")
                    return
          print("Book not found.")



library = Library()

while True:
     print("\nLibrary Management System")
     print("1. Add Book")
     print("2. Display Books")
     print("3. Search Book")
     print("4. Borrow Book")
     print("5. Return Book")
     print("6. Exit")

     choice = input("Enter your choice: ")

     if choice == "1":
          library.add_book()
     elif choice == "2":
          library.display_books()
     elif choice == "3":
          library.search_book()
     elif choice == "4":
          library.borrow_book()
     elif choice == "5":
          library.return_book()
     elif choice == "6":
          print("Goodbye!")
          break
     else:
          print("Invalid choice.")
