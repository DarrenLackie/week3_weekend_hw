from flask import render_template, Blueprint
from models.book import Book
from models.book_list import books

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route('/books')
def index():
    return render_template("index.jinja", title="Book List", books=books)