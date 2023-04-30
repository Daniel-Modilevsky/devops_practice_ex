from flask import Flask

from controllers.controller_dashboard import dashboard
from controllers.controller_login import login

app = Flask(__name__)
app.secret_key = "your_secret_key_here"


# Routes
@app.route('/')
def index():
    return 'Welcome to the Auth test server.'


app.route('/login', methods=['GET', 'POST'])(login)
app.route('/dashboard', methods=['GET'])(dashboard)


app.run(host='0.0.0.0', port=5050, debug=True)
