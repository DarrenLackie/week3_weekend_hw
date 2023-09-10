from flask import render_template, Blueprint, redirect, request
from models.book import Book
from models.book_list import books, add_new_book, remove_book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def index():
    return render_template("index.jinja", title="Book List", books=books)

@books_blueprint.route('/books/contact')
def contact():
   return render_template("contact.jinja", title="Contact", books=books)

@books_blueprint.route('/books/about')
def about():
   return render_template("about.jinja", title="About", books=books)

@books_blueprint.route('/books/<index>')
def show(index):
  chosen_book = books[int(index)]
  return render_template('books.jinja', book=chosen_book)

@books_blueprint.route('/books', methods=["POST"])
def add_book():
   title = request.form['title']
   author = request.form['author']
   genre = request.form['genre']
   checked_out = True if 'checked_out' in request.form else False
   new_book = Book(title=title, author=author, genre=genre, checked_out=checked_out)
   add_new_book(new_book)
   return redirect('/books')

@books_blueprint.route('/books/delete/<title>', methods=['POST'])
def delete(title):
   remove_book(title)
   return redirect('/books')