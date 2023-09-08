from models.book import Book

book1 = Book("Pet Sematary", "Stephen King", "Horror", True)
book2 = Book("Annihilation", "Jeff VanderMeer", "Sci-Fi", False)

books = [book1, book2]

def add_new_book(book):
    books.append(book)

def remove_book(book_name):
    book_to_delete = None
    for book in books:
        if book.title == book_name:
            book_to_delete = book
            books.remove(book_to_delete)