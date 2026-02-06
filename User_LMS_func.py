users = {}
books = {}
borrow = {}

def operation(method):
     username = input("Enter your username: ")
     password = input("Enter your password: ")

     if method == "register":
          if username in users:
               print("User already exists.")
          else:
               users[username] = {"password": password}
               print("Registered successfully!")

     elif method == "login":
          if username in users and users[username]["password"] == password:
               print("Login successful!")
               return username
          elif username in users:
               print("Incorrect password.")
          else:
               print("User not found.")
     return None


def add_book():
     book_id = input("Enter Book ID: ")
     if book_id in books:
          print("Book already exists.")
          return

     title = input("Enter book title: ")
     author = input("Enter book author: ")

     books[book_id] = {
          "title": title,
          "author": author,
          "available": True
     }
     print(f"Book '{title}' added successfully!")


def display_book():
     if not books:
               print("No books available.")
               return

     for book_id, info in books.items():
          status = "Available" if info["available"] else f"Borrowed by {borrow.get(book_id)}"
          print(f"ID: {book_id} | Title: {info['title']} | Author: {info['author']} | {status}")


def search_book():
     keyword = input("Enter book ID or title: ").lower()
     found = False

     for book_id, info in books.items():
          if keyword in book_id.lower() or keyword in info["title"].lower():
               status = "Available" if info["available"] else "Borrowed"
               print(f"Found → {book_id} | {info['title']} | {info['author']} | {status}")
               found = True

     if not found:
          print("Book not found.")


def display_members():
     if not users:
               print("No registered members.")
               return

     for user in users:
          print("Username:", user)


def borrow_book(username):
     book_id = input("Enter Book ID to borrow: ")

     if book_id not in books:
          print("Book not found.")
          return

     if not books[book_id]["available"]:
          print("Book already borrowed.")
          return

     books[book_id]["available"] = False
     borrow[book_id] = username
     print("Book borrowed successfully!")


def return_book(username):
     book_id = input("Enter Book ID to return: ")

     if book_id not in books:
          print("Book not found.")
          return

     if books[book_id]["available"]:
          print("This book is not borrowed.")
          return

     if borrow.get(book_id) != username:
          print("You did not borrow this book.")
          return

     books[book_id]["available"] = True
     del borrow[book_id]
     print("Book returned successfully!")


def LMS_operation(username):
     while True:
          print("\n--- Library Menu ---")
          print("1. Add Book")
          print("2. Display Books")
          print("3. Search Book")
          print("4. Display Members")
          print("5. Borrow Book")
          print("6. Return Book")
          print("7. Logout")

          choice = input("Enter choice: ")

          match choice:
               case "1":
                    add_book()
               case "2":
                    display_book()
               case "3":
                    search_book()
               case "4":
                    display_members()
               case "5":
                    borrow_book(username)
               case "6":
                    return_book(username)
               case "7":
                    break
               case _:
                    print("Invalid choice.")


while True:
     print("\n1. Register\n2. Login\n3. Exit")
     choice = input("Choose option: ")

     match choice:
          case "1":
               operation("register")
          case "2":
               user = operation("login")
               if user:
                    LMS_operation(user)
          case "3":
               print("Goodbye!")
               break
          case _:
               print("Invalid choice.")
