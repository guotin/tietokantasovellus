from application import db
from sqlalchemy.sql import text


class Review(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(500), nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, grade, text):
        self.grade = grade
        self.text = text

    @staticmethod
    def find_reviews_for_book(book_id):
        stmt = text("SELECT account.username as username, book.name as bookname, review.grade as grade, review.id, "
                    " review.text as reviewtext FROM review"
                    " JOIN account ON account.id = review.account_id"
                    " JOIN book ON book.id = review.book_id"
                    " WHERE book.id = :bookid ")
        
        res = db.engine.execute(stmt, bookid = book_id)
        response = []
        for row in res:
            response.append(row)

        return response
