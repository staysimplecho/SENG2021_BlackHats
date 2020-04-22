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

def get_eventdata():
    global events
    return events
SECRET = "MISHMASH" # The secret to encode token
# User class to store data on users
events = []
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.u_id = 0
        self.username = 'anonymity'
        self.state = 0  # 0 - Unregistered, 1 - Registered/Logged in, 2 - Logged Out
        self.reset_code = None
        self.profile_image = ''
        self.channels = []
        self.status = 3 # 1 - SLACKR Owner, 2 - Admin, 3 - Member

class Event:
    def __init__(self, genre, singer, date):
        self.genre = genre
        self.singer = singer
        self.date = date
        self.e_id = 0
        self.comments = ''

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

@app.route("/login", methods=["POST"])
def auth_login():
    users = get_data()
    email = request.form.get("email")
    # CHECKS FOR INVALID INFORMATION BELOW
    result = valid_email(email)
    if result == 1:
        raise ValueError(f"Email is not registered.")
    elif result == 0:
        raise ValueError(f"Invalid Email.")
    # Finding u_id associated with token
    user = get_user_for_email(email)
    
    # Checking matching passwords
    input_password = request.form.get("password")
    input_password = hashpass(input_password)
    if input_password != user.password:
        raise ValueError(f"Password is incorrect.")
    #if (user.state == 1):
    #    raise ValueError(f"User is already logged in.")
    # CHECKS FOR INVALID INFROMATION ABOVE

    # Getting user corresponding to token
    user.token = get_token(user.u_id)
    user.state = 1 # Setting state to logged in
    return dumps({"u_id" : user.u_id, "token" : user.token})
# LOGOUT FUNCTION
@app.route("/logout", methods=["POST"])
def auth_logout():
    token = request.form.get("token")
    user = get_user_for_token(token)    # Finding user for given token
    if user is None:                    # If there is no user corresponding to token
        return dumps({"is_success" : False})
    if user.state==2:               # If user is already logged out
        return dumps({"is_success" : False})
    user.state = 2                      # Changing the user's state to logged out
    return dumps({"is_success" : True})

# PASSWORD RESET REQUEST FUNCTION
@app.route("/passwordreset", methods=["POST"])
def auth_passwordreset_reset():
    users = get_data()
    token = request.form.get("token")
    user = get_user_for_token(token)    # Finding user for given token
    if user is None:                    # If there is no user corresponding to token
        return dumps({"is_success" : False})
    new_password = request.form.get("password")
    if user is None:
        raise ValueError(f"Invalid reset code.")
    # Check whether the password given is valid
    if len(new_password) > 5:
        user.password = hashpass(new_password)
    else:
        raise ValueError(f"Invalid password.")       # Resetting reset code to None
    return dumps({"is_success" : True})

@app.route("/user/profile/setemail", methods=['PUT'])
def setemail():
    token = request.form.get('token')
    email = request.form.get('email') 
    user = get_user_for_token(token)
    #check if the email is valid
    result = valid_email(email) 
    if result == -1:
        raise ValueError(f"Email is already in use.") 
    else:
        raise ValueError(f"Invalid Email.") 
    user.email = email
    return dumps({"is_success" : True})

@app.route("/setusername", methods=["PUT"])
#PUT user/profile/setname (token, name_first, name_last) 
def user_setname():
    users = get_data()
    token = request.form.get("token")
    # check the length of frist name and last name
    username = request.form.get("username")
    if len(username) < 1 or len(username) > 50:
        raise ValueError(f"username must be between 1 and 50 characters.") 
    user = get_user_for_token(token)
    user.username = username
    return dumps({"is_success" : True})

@app.route("/add_event", methods=["POST"])
def add_event():
    events = get_eventdata()
    genre = request.form.get("genre")
    singer = request.form.get("singer")
    date = request.form.get("date")
    # CHECKS FOR INVALID INFORMATION BELOW
    # Checking whether email is valid
    e_id = create_e_id()
    # Creating a user and setting variables of the user
    event = Event(genre, singer,date)       # User is set to logged in state
    event.e_id = int(e_id)
    # If this is the first account to register, they are set as admin
    events.append(event)      # Appending the user to the list of users
    return dumps({"e_id" : int(e_id)})

@app.route("/add_comment", methods=["POST"])
def add_comment():
    events = get_eventdata()
    e_id = request.form.get("e_id")
    event = get_event_for_e_id(e_id)
    comment = request.form.get("comment")
    if len(comment) < 1 or len(comment) > 50:
        raise ValueError(f"comment must be between 1 and 50 characters.") 
    e_id = create_e_id()
    # Creating a user and setting variables of the user
    event = Event(genre, singer,date)       # User is set to logged in state
    event.e_id = int(e_id)
    # If this is the first account to register, they are set as admin
    events.append(event)      # Appending the user to the list of users
    return dumps({"e_id" : int(e_id)})

def create_u_id():
    global users
    return str(len(users) + 1).zfill(5)
def create_e_id():
    global events
    return str(len(events) + 1).zfill(5)
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

def get_event_for_e_id(e_id):
    global events
    for event in events:
        if (event.e_id == e_id):
            return event
    return None
if __name__ == '__main__':
    app.run(port=6000)
