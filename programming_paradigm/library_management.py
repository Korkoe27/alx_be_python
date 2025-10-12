class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def __repr__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"<Book: {self.title} by {self.author} - {status}>"


class Library:
    def __init__(self):
        # ✅ Use _books (private attribute) as required
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Added: {book}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                print(f"Checked out: {book.title}")
                return True
        print(f"Book titled '{title}' not found or already checked out.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                print(f"Returned: {book.title}")
                return True
        print(f"Book titled '{title}' not found or not checked out.")
        return False

    def list_available_books(self):
        available = [book for book in self._books if not book._is_checked_out]
        print("Available books:")
        print(available)