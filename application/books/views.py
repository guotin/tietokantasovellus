from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from application import app, db

from application.books.models import Book
from application.books.forms import BookForm, UpdateForm
from application.auth.models import UserBook
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

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
    elif "update" in request.form:
        return books_update(book_id)
    else:
        return redirect(url_for("books_index"))

@app.route("/books/update/<book_id>/", methods=["GET", "POST"])
@login_required
def books_update(book_id):

    book = Book.query.get(book_id)
    form = UpdateForm(obj=book)

    if form.validate_on_submit():
        form.populate_obj(book)
        db.session().commit()
        
    return render_template("books/update.html", book=book, form=form)
  
@app.route("/books/<book_id>/", methods=["POST"])
@login_required
def books_delete(book_id):
    
    book = Book.query.get(book_id)
    db.session.delete(book)
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
