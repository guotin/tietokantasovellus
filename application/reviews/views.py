from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
from application import app, db, login_required

from application.reviews.models import Review
from application.reviews.forms import ReviewForm
from application.auth.models import Account

@app.route("/reviews/mylist/<review_id>/", methods=["GET", "POST"])
def reviews_contact(review_id):
    if "delete" in request.form:
        return reviews_delete(review_id)
    elif "update" in request.form:
        return reviews_update(review_id)
    else:
        return redirect(url_for("reviews_private_list"))

@app.route("/reviews/mylist", methods=["GET"])
@login_required(role="ANY")
def reviews_private_list():
    
    reviews = Account.find_users_reviews(current_user.id)
    return render_template("reviews/mylist.html", reviews=reviews)

@app.route("/reviews/mylist/<review_id>/", methods=["POST"])
@login_required(role="ANY")
def reviews_delete(review_id):
    
    review = Review.query.get(review_id)
    db.session.delete(review)
    db.session().commit()

    return redirect(url_for("reviews_private_list"))

@app.route("/reviews/update/<review_id>/", methods=["GET","POST"])
def reviews_update(review_id):

    review = Review.query.get(review_id)
    form = ReviewForm(obj=review)

    if form.validate_on_submit():
        form.populate_obj(review)
        db.session().commit()

    return render_template("reviews/update.html", review=review, form=form)
