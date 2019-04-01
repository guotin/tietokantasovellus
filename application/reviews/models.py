from application import db


class Review(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(500), nullable=False)

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, grade, text):
        self.grade = grade
        self.text = text

