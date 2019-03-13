from flask import render_template, request, redirect, url_for
from application import app, db
from application.books.models import Book

@app.route("/books", methods=["GET"])
def books_index():
    return render_template("books/list.html", books = Book.query.all())
                           
@app.route("/books/new/")
def books_form():
    return render_template("books/new.html")

@app.route("/books/<book_id>/", methods=["POST"])
def book_set_year(book_id):

    t = Book.query.get(book_id)
    t.publication_year = request.form['year']
    db.session().commit()

    return redirect(url_for("books_index"))
    
@app.route("/books/", methods=["POST"])
def books_create():
    
    name = request.form['name']
    author = request.form['author']
    publication_year = request.form['publication_year']
    
    t = Book(name, author, publication_year)
    db.session().add(t)
    db.session().commit()
    
    return redirect(url_for("books_index"))                       
