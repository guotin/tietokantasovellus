from application import db
from sqlalchemy.sql import text

class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    
    users = db.relationship("AccountBook", cascade="all, delete-orphan")
    reviews = db.relationship("Review", backref="book", lazy=True, cascade="all, delete-orphan")

    def __init__(self, name, author, publication_year):
        self.name = name
        self.author = author
        self.publication_year = publication_year

    @staticmethod
    def find_books_users(book_id):
        stmt = text("SELECT account.username, account.password FROM account"
                    " JOIN account_book ON account_book.account_id = account.id"
                    " WHERE account_book.book_id = :bookid ")
        
        res = db.engine.execute(stmt, bookid = book_id)
        response = []
        for row in res:
            response.append(row)

        return response

    @staticmethod
    def find_most_read_books():
        stmt = text("SELECT DISTINCT book.name, book.author, book.publication_year,"
                    " (SELECT COUNT(id) FROM account JOIN account_book ON account_book.account_id = account.id WHERE account_book.book_id = book.id)"
                    " AS times_read FROM book"
                    " WHERE (SELECT COUNT(id) FROM account JOIN account_book ON account_book.account_id = account.id WHERE account_book.book_id = book.id) > 0"
                    " ORDER BY times_read DESC"
                    " LIMIT 5")
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)

        return response
    
    @staticmethod
    def find_best_graded_books():
        stmt = text("SELECT DISTINCT book.name, book.author, book.publication_year,"
                    " (SELECT SUM(review.grade) FROM review WHERE review.book_id = book.id) AS grade_sum,"
                    " (SELECT COUNT(review.id) FROM review WHERE review.book_id = book.id) AS grade_count,"
                    " (SELECT SUM(review.grade) * 1.0 / COUNT(review.id) FROM review WHERE review.book_id = book.id) AS grade_order"
                    " FROM book"
                    " WHERE (SELECT COUNT(review.id) FROM review WHERE review.book_id = book.id) > 0"
                    " ORDER BY grade_order DESC"
                    " LIMIT 5")
        
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)

        return response
    

    
