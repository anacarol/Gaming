from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World!'



@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'




@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


# /login
# /login?next=/
# /user/Ana%Assis



# $ export FLASK_APP=hello.py
# export FLASK_ENV=development. (???)
# $ python -m flask run
#  * Running on http://127.0.0.1:5000/






################### ***************************** ###################
# Externally Visible Server
# If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.

# If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

# flask run --host=0.0.0.0
# This tells your operating system to listen on all public IPs.
################### ***************************** ###################