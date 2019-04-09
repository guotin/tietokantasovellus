from application import db
from application.books.models import Book

from sqlalchemy.sql import text


class AccountBook(db.Model):
    __table_args__ = (db.PrimaryKeyConstraint('account_id', 'book_id'),)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, account_id, book_id):
        self.account_id = account_id
        self.book_id = book_id


class Account(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    books = db.relationship("AccountBook", backref='book', lazy=True, cascade="all, delete-orphan")
    reviews = db.relationship("Review", backref='review', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.admin = False;

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.admin:
            return ["ADMIN"]
        
        return ["USER"]

    @staticmethod
    def find_users_with_most_reviews():
        stmt = text("SELECT Account.username, COUNT(Review.id) FROM Account"
                    " JOIN Review ON Review.account_id = Account.id"
                    " WHERE Review.account_id = Account.id"
                    " GROUP BY Account.username"
                    " ORDER BY COUNT(Review.id) DESC"
                    " LIMIT 5")
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"username":row[0], "reviews":row[1]})

        return response

    @staticmethod
    def find_users_books(account_id):
        stmt = text("SELECT * FROM book"
                    " JOIN account_book ON account_book.book_id = book.id"
                    " WHERE account_book.account_id = :accountid ")
        
        res = db.engine.execute(stmt, accountid = account_id)
        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def find_users_reviews(account_id):
        stmt = text("SELECT book.name as bookname, review.id as id, review.grade as grade, review.text as reviewtext FROM review"
                    " JOIN account ON account.id = review.account_id"
                    " JOIN book ON book.id = review.book_id"
                    " WHERE account.id = :accountid ")
        
        res = db.engine.execute(stmt, accountid = account_id)
        response = []
        for row in res:
            response.append(row)

        return response
