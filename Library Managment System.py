# Book class to store title, author and borrowed status
class Book:

    def __init__(self, title, author):
        self.Title = title
        self.Author = author
        self.Is_borrowed = False  # Book is available at the start

    def borrow(self):
        if not self.Is_borrowed:
            self.Is_borrowed = True
            print(f"You borrowed '{self.Title}' by {self.Author}.")
        else:
            print(f"Sorry, '{self.Title}' is already borrowed.")

    def return_book(self):
        if self.Is_borrowed:
            self.Is_borrowed = False
            print(f"'{self.Title}' by {self.Author} has been returned.")
        else:
            print(f"'{self.Title}' by {self.Author} was not borrowed.")

    def status_display(self):
        status = "Available" if not self.Is_borrowed else "Borrowed"
        print(f"'{self.Title}' by {self.Author} - {status}")


# List of books
books_data = [
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("Moby-Dick", "Herman Melville"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Brave New World", "Aldous Huxley"),
]

# Create book objects and store in a list
library = []
for title, author in books_data:
    library.append(Book(title, author))

# Menu items
menu_items = [
    "===== Library Menu =====",
    "1. Check all books",
    "2. Borrow a book",
    "3. Return a book",
    "4. Exit",
]

# Start the program loop
while True:
    # Show menu
    for item in menu_items:
        print(item)

    user = input("Select the option: ")

    try:
        if user.isdigit():
            choice = int(user)

            if choice == 1:
                # Show all books
                for idx, book in enumerate(library, start=1):
                    print(f"{idx}. ", end="")
                    book.status_display()

            elif choice == 2:
                # Borrow a book
                book_num = int(input("Enter book number to borrow: "))
                if 1 <= book_num <= len(library):
                    library[book_num - 1].borrow()
                else:
                    print("Invalid book number!")

            elif choice == 3:
                # Return a book
                book_num = int(input("Enter book number to return: "))
                if 1 <= book_num <= len(library):
                    library[book_num - 1].return_book()
                else:
                    print("Invalid book number!")

            elif choice == 4:
                # Exit
                print("Exiting Library. Goodbye!")
                break  # Exit the while loop

            else:
                print("Invalid choice! Please select 1-4.")

        else:
            print("Invalid input! Enter a number 1-4.")

    except ValueError:
        print("Invalid number! Please enter digits only.")
