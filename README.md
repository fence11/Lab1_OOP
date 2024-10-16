﻿# Lab1_OOP - TI-231
## Classes
1. Book
Represents a book with attributes:

+ `title (str)`: book title;
+ `author (str)`: book author;
+ `book_id (int)`: unique ID for every book, incremented per book added.

### Methods:
`__repr__(self)`: string representation of the book in the following format: 
`Book(ID: <book_id>, Title: '<title>', Author: '<author>')`.

book = Book("title", "author", 1)
print(book)
will print: ID: 1, Title: title, Author: author


2. Library
Represents a library with methods to add, display or remove the books.

### Methods:
+ `__init__(self)`: Initializes the library with an empty list and a starting ID of 1

+ `add_book(self)`: Prompts the user to input the title and author and creates a <Book>, assigns a unique ID to it, then appends it to the list.

+ `remove_book(self, book_id)`: Removes a book by its book_id. If no book with the given book_id exists, it displays a message.

+ `display_books_by_author(self, author)`: Displays all books by the specified author. If no book with the given author or the author themselves doesn't exist, it displays a message.

+ `display_book_by_id(self, book_id)`: Displays a specific book by its book_id. If no book with the given book_id exists, it displays a message.

+ `display_all_books(self)`: Displays all books currently in the library. If the library is empty, it displays a message.
