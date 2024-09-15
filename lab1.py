class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id

    def __str__(self):
        return f"Book(ID: {self.book_id}, Title: '{self.title}', Author: '{self.author}')"


class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        new_book = Book(title, author, self.next_id)
        self.books.append(new_book)
        print(f"Book '{new_book.title}' by {
              new_book.author} added to the library with ID {new_book.book_id}.")
        self.next_id += 1

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ID {book_id} not found.")

    def display_books_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)

        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found by {author}.")

    def display_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print(book)
                return
        print(f"Book with ID {book_id} not found.")

    def display_all_books(self):
        if not self.books:
            print("The library is currently empty.")
        else:
            print("Library books:")
            for book in self.books:
                print(book)


library = Library()

while True:
    print("\n1. Display all books\n"
          "2. Display books by an author\n"
          "3. Display books by ID\n"
          "4. Remove books by ID\n"
          "5. Add more books to library\n"
          "0. Exit\n")

    try:
        choice = int(input("Input a choice: "))
    except ValueError:
        print("Invalid value. Try again.")
        continue

    if choice == 1:
        library.display_all_books()
    elif choice == 2:
        author_name = input("Find books by author name: ")
        library.display_books_by_author(author_name)
    elif choice == 3:
        try:
            book_id = int(input("Find book by ID: "))
            library.display_book_by_id(book_id)
        except ValueError:
            print("Invalid number for book ID.")
    elif choice == 4:
        try:
            book_id = int(input("Remove book by ID: "))
            library.remove_book(book_id)
        except ValueError:
            print("Invalid number for book ID.")
    elif choice == 5:
        try:
            number_of_books = int(input("Number of books to add: "))
            for _ in range(number_of_books):
                library.add_book()
        except ValueError:
            print("Invalid value.")
    elif choice == 0:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice number. Try again.")
