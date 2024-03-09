from flask import Blueprint
from flask import render_template


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("base.html")

@views.route('/dashboard')
def dashboard():
    # Your profile page logic here
    return render_template('dashboard.html')

@views.route('/profile')
def profile():
    # Your profile page logic here
    return render_template('profile.html')

@views.route('/mot_de_pass')
def mot_de_pass():
    # Your profile page logic here
    return render_template('mot_de_pass.html')

@views.route('/ESN')
def esn():
    # Your profile page logic here
    return render_template('esn.html')

@views.route('/Entreprises')
def entreprises():
    # Your profile page logic here
    return render_template('entreprises.html')


@views.route('/Contact_us')
def contactus():
    # Your profile page logic here
    return render_template('contactus.html')

@views.route('/404')
def erreur():
    # Your profile page logic here
    return render_template('404.html')

@views.route('/login')
def login():
    # Your profile page logic here
    return render_template('login.html')


