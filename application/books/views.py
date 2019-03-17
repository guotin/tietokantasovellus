from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.books.models import Book
from application.books.forms import BookForm, UpdateForm
from application.auth.models import UserBook

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())
                           
@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form = BookForm())

@app.route("/books/<book_id>/", methods=["GET", "POST"])
@login_required
def books_contact(book_id):
    if "delete" in request.form:
        return books_delete(book_id)
    elif "update_name" in request.form:
        return books_set_name(book_id)
    elif "update_author" in request.form:
        return books_set_author(book_id)
    elif "update_publication_year" in request.form:
        return books_set_publication_year(book_id)
    else:
        return redirect(url_for("books_index"))
    
@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_delete(book_id):
    
    book = Book.query.get(book_id)
    userbook_delete = UserBook.__table__.delete().where(UserBook.book_id == book_id)
    db.session.execute(userbook_delete)
    db.session.delete(book)
    db.session().commit()

    return redirect(url_for("books_index"))


@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_set_name(book_id):

    book = Book.query.get(book_id)
    book.name = request.form['name']
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_set_author(book_id):

    book = Book.query.get(book_id)
    book.author = request.form['author']
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_set_publication_year(book_id):

    book = Book.query.get(book_id)
    book.publication_year = request.form['publication_year']
    db.session().commit()

    return redirect(url_for("books_index"))
    
@app.route("/books/", methods=["POST"])
@login_required
def books_create():

    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)
    
    name = form.name.data
    author = form.author.data
    publication_year = form.publication_year.data
    
    book = Book(name, author, publication_year)
    db.session().add(book)
    db.session().commit()
    
    #Add an entry to table "UserBook" with current user id and the new book id
    bookuser = UserBook(current_user.id, book.id)
    db.session().add(bookuser)
    db.session().commit()
    
    return redirect(url_for("books_index"))                       
