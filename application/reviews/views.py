from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from application import app, db

from application.reviews.models import Review
from application.reviews.forms import ReviewForm

@app.route("/reviews", methods=["GET"])
def reviews_index():
    return render_template("reviews/list.html", books = Book.query.all())

