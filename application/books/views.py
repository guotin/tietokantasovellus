from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from application import app, db, login_required

from application.books.models import Book
from application.books.forms import BookForm
from application.auth.models import Account, AccountBook
from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/books", methods=["GET"])
def books_index():  
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/mylist", methods=["GET"])
@login_required(role="ANY")
def books_personal_list():
       
    book_list = Account.find_users_books(current_user.id)                     
    return render_template("books/mylist.html", books = book_list)

@app.route("/books/mostread", methods=["GET"])
def books_most_read():
    return render_template("books/mostread.html", books = Book.find_most_read_books())
                           
@app.route("/books/new/")
@login_required(role="ANY")
def books_form():
    return render_template("books/new.html", form = BookForm())

@app.route("/books/<book_id>/", methods=["GET", "POST"])
def books_contact(book_id):
    if "delete" in request.form:
        return books_delete(book_id)
    elif "update" in request.form:
        return books_update(book_id)
    elif "review" in request.form:
        return reviews_create(book_id)
    elif "list" in request.form:
        return reviews_list(book_id)
    elif "mark" in request.form:
        return books_mark_as_read(book_id)
    elif "privatedelete" in request.form:
        return books_delete_from_personal_list(book_id)
    else:
        return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["GET","POST"])
@login_required(role="ANY")
def books_mark_as_read(book_id):

    account_list = Book.find_books_users(book_id)                            
    for account in account_list:
        if current_user.username == account.username:
            return redirect(url_for("books_index"))
        
    new_relation = AccountBook(current_user.id, book_id)
    db.session().add(new_relation)
    db.session().commit()
        
    return redirect(url_for("books_index"))

@app.route("/books/<book_id>/", methods=["GET","POST"])
@login_required(role="ANY")
def books_delete_from_personal_list(book_id):
    
    primary_key = (current_user.id, book_id)
    relationship = AccountBook.query.get(primary_key)
    db.session.delete(relationship)
    db.session().commit()

    return redirect(url_for("books_personal_list"))

@app.route("/books/update/<book_id>/", methods=["GET", "POST"])
@login_required(role="ANY")
def books_update(book_id):

    book = Book.query.get(book_id)
    form = BookForm(obj=book)

    if form.validate_on_submit():
        form.populate_obj(book)
        db.session().commit()
                
    return render_template("books/update.html", book=book, form=form)
  
@app.route("/books/<book_id>/", methods=["POST"])
@login_required(role="ADMIN")
def books_delete(book_id):
    
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session().commit()

    return redirect(url_for("books_index"))

    
@app.route("/books/", methods=["POST"])
@login_required(role="ANY")
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
    
    #Add an entry to table "AccountBook" with current user id and the new book id
    bookuser = AccountBook(current_user.id, book.id)
    db.session().add(bookuser)
    db.session().commit()
    
    return redirect(url_for("books_index"))

@app.route("/reviews/<book_id>", methods=["POST"])
@login_required(role="ANY")
def reviews_create(book_id):

    form = ReviewForm(request.form)
    book = Book.query.get(book_id)
  
    if not form.validate():
        return render_template("reviews/new.html", form = form, book=book)
    
    review = Review(form.grade.data, form.text.data)
    review.book_id = book_id
    review.account_id = current_user.id
    db.session().add(review)
    db.session().commit()

    return redirect(url_for("books_personal_list"))

@app.route("/reviews", methods=["GET"])
def reviews_list(book_id):
    
    reviews = Review.find_reviews_for_book(book_id)
    book = Book.query.get(book_id)  
    return render_template("reviews/list.html", reviews=reviews, bookname=book.name)
    
    
                
