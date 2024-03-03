from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")

@views.route('/profile')
def profile():
    # Your profile page logic here
    return render_template('profile.html')

@views.route('/dashboard')
def dashboard():
    # Your profile page logic here
    return render_template('dashboard.html')
