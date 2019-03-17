from application import db


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    author = db.Column(db.String(144), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
    users = db.relationship("UserBook")

    def __init__(self, name, author, publication_year):
        self.name = name
        self.author = author
        self.publication_year = publication_year
