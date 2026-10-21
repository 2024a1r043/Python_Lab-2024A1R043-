#Write a python program that allows a librarian to add several books to a librrary. For each book, ask the user to enter its title and the number of copies. Store each book and its available copy ccount in a dictionary.
#After the books have been added, display a menu that let the user issue a book, return a book, display all books, or exit the program.
#Apply these conditions:
#Book titles should be compared without distinguishing between uppercase and lowercase letters.
#A book can be issued only if it exists in the library and at least one copy is available.
#Issuing a book decreases its available copy count by one.
#A book can be returned only if it exists in the library and at least one copy has already been issued.
#Returning a book increases its available copy count by one.
#Display an appropriate message for an unavailable book, an invalid choice, or an invalid number of copies.
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        key = title.lower()
        self.books[key] = [title, copies, copies]

    def issue_book(self, title):
        key = title.lower()

        if key not in self.books:
            print("Book does not exist in the library.")
        elif self.books[key][1] == 0:
            print("Book is not available.")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully.")

    def return_book(self, title):
        key = title.lower()

        if key not in self.books:
            print("Book does not exist in the library.")
        elif self.books[key][1] == self.books[key][2]:
            print("No copies of this book have been issued.")
        else:
            self.books[key][1] += 1
            print("Book returned successfully.")

    def display_books(self):
        for title, (original_title, available_copies, total_copies) in self.books.items():
            print(f"{original_title}: {available_copies} copies")


library = Library()

n = int(input("Enter number of books: "))

for i in range(n):
    title = input("Enter book title: ")
    copies = int(input("Enter number of copies: "))
    library.add_book(title, copies)

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        library.issue_book(title)

    elif choice == "2":
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == "3":
        library.display_books()

    elif choice == "4":
        print("Exiting library system.")
        break

    else:
        print("Invalid choice.")
