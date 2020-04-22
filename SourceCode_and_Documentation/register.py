"""Flask server"""
import sys
from json import dumps
from datetime import datetime
import time
import uuid
import re
import hashlib
from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from werkzeug.exceptions import HTTPException
import jwt
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
# SETUP OF ERROR HANDLER BELOW
app = Flask(__name__)
CORS(app)
# SETUP OF ERROR HANDLER ABOVE
# SETUP OF EMAIL BELOW
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='slackrskywalkers@gmail.com',
    MAIL_PASSWORD="Blabla5!"
)
# SETUP OF EMAIL ABOVE
# registered_users = {} # {u_id : email, token}
users = []
# Function to use users in other functions
def get_data():
    global users
    return users
SECRET = "MISHMASH" # The secret to encode token
# User class to store data on users
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.u_id = 0
        self.handle = 'anonymity'
        self.state = 0  # 0 - Unregistered, 1 - Registered/Logged in, 2 - Logged Out
        self.reset_code = None
        self.profile_image = ''
        self.channels = []
        self.status = 3 # 1 - SLACKR Owner, 2 - Admin, 3 - Member
@app.route('/echo/get', methods=['GET'])
def echo1():
    """ Description of function """
    return dumps({
        'echo' : request.args.get('echo'),
    })
@app.route('/echo/post', methods=['POST'])
def echo2():
    """ Description of function """
    return dumps({
        'echo' : request.form.get('echo'),
    })
#####################################################################################
#                                                                                   #
#                               AUTHENTICATION FUNCTIONS                            #
#                                                                                   #
#####################################################################################
# REGISTRATION FUNCTION
@app.route("/register", methods=["POST"])
def auth_register():
    users = get_data()
    email = request.form.get("email")   # Getting the email from server
    # CHECKS FOR INVALID INFORMATION BELOW
    # Checking whether email is valid
    result = valid_email(email)
    if result == -1:
        raise ValueError("Exisited Email.")
    elif result == 0:
        raise ValueError("Invalid Email.")
    password = request.form.get("password")
    if len(password) < 5:
        raise ValueError(f"Password is too short.")
    password = hashpass(password)       # Hashing the password for storage
    # CHECKS FOR INVALID INFORMATION ABOVE
    u_id = create_u_id()
    # Creating a user and setting variables of the user
    user = User(email, password)
    user.state = 1          # User is set to logged in state
    user.u_id = int(u_id)
    token = get_token(u_id) # Getting token
    user.token = token
    # If this is the first account to register, they are set as admin
    if (len(users) == 0):
        user.status = 1     # setting owner
    users.append(user)      # Appending the user to the list of users
    return dumps({"u_id" : int(u_id), "token" : token})

def create_u_id():
    global users
    return str(len(users) + 1).zfill(5)
def get_token(u_id):
    curr_time = datetime.now()
    token = jwt.encode({ "u_id" : u_id, "time" : curr_time.isoformat()}, SECRET, algorithm='HS256').decode('utf-8')
    return token
def valid_email(email):
    if re.search(regex, email):
        user = get_user_for_email(email)
        if user is None:
            return 1    # email not in use
        else:
            return -1   # returns -1 for existing email
    else:
        return 0    # returns 0 for invalid email
def gen_reset_code():
    reset_code = uuid.uuid4().hex
    return reset_code
def valid_token(token):
    user = get_user_for_token(token)
    if user.state == 2 and user.state == 0:
        return False
    else:
        return True
def hashpass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_for_email(email):
    global users
    for user in users:
        if (user.email == email):
            return user
    return None

def get_user_for_token(token):
    global users
    for user in users:
        if (user.token == token):
            return user
    return None
if __name__ == '__main__':
    app.run(port=6000)
