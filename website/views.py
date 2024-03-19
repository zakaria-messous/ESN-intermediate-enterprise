from flask import Blueprint
from flask import render_template
from flask import Flask, request, redirect, url_for
from flask_cognito import CognitoAuth


views = Blueprint('views', __name__)


@views.route('/base')
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

@views.route("/loggedin", methods=["GET"])
def logged_in():
    access_token = aws_auth.get_access_token(request.args)
    resp = make_response(redirect(url_for('login.html')))
    set_access_cookies(resp, access_token, max_age=30 * 60)
    return resp


# Replace with your actual Cognito pool details
app = Flask(_name_)
app.config['COGNITO_USER_POOL_ID'] = 'your_user_pool_id'
app.config['COGNITO_CLIENT_ID'] = 'your_client_id'
app.config['COGNITO_DOMAIN'] = 'your_cognito_domain'
app.config['COGNITO_REDIRECT_URI'] = 'http://localhost:5000/callback'  # Adjust port if needed

cognito = CognitoAuth(app)

@app.route('/')
def index():
  if cognito.user_authenticated:
    return f"Welcome, {cognito.user['username']}!"
  else:
    return redirect(url_for('login'))

@app.route('/login')
def login():
  login_url = cognito.authorize_url(
      responseType='code',
      scope='openid email'  # Add additional scopes if needed
  )
  return redirect(login_url)