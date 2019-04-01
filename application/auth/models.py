from application import db
from application.books.models import Book

from sqlalchemy.sql import text


class UserBook(db.Model):
    __table_args__ = (db.PrimaryKeyConstraint('user_id', 'book_id'),)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    books = db.relationship("UserBook", backref='book', lazy=True)
    reviews = db.relationship("Review", backref='review', lazy=True)

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_most_reviews():
        stmt = text("SELECT User.username, COUNT(Review.id) FROM User"
                    " JOIN Review ON Review.user_id = User.id"
                    " WHERE Review.user_id = User.id"
                    " GROUP BY User.username"
                    " ORDER BY COUNT(Review.id) DESC"
                    " LIMIT 5")
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"username":row[0], "reviews":row[1]})

        return response
