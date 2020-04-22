import sys
sys.path.insert(0, 'server')
from werkzeug.exceptions import HTTPException
from db import sendSuccess, data, getUserFromToken
from comment import *
from user import *
from auth import *
from flask import Flask, request, jsonify, send_from_directory
from flask_mail import Mail, Message
from json import dumps
from flask_cors import CORS

def defaultHandler(err):
    response = err.get_response()
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.description,
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__, static_url_path='/static/')
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(HTTPException, defaultHandler)
CORS(APP)

@APP.route('/auth/register', methods=['POST'])
def register_auth():
    # arguments
    email = request.form.get('email')
    password = request.form.get('password')
    username = request.form.get('username')

    registerDict = auth_register(email, password, username)
    return sendSuccess({
        'u_id': registerDict['u_id'],
        'token': str(registerDict['token']),
    })


@APP.route('/auth/login', methods=['POST'])
def login_auth():
    loginDict = auth_login(request.form.get(
        'email'), request.form.get('password'))

    return sendSuccess({
        'u_id': loginDict['u_id'],
        'token': str(loginDict['token'])
    })


@APP.route('/auth/logout', methods=['POST'])
def logout_auth():
    is_success = auth_logout(request.form.get('token'))
    return sendSuccess({'is_success' : is_success})

# APP.config.update(
#     MAIL_SERVER='smtp.gmail.com',
#     MAIL_PORT=465,
#     MAIL_USE_SSL=True,
#     MAIL_USERNAME = 'two.oh.oh@gmail.com',
#     MAIL_PASSWORD = "Brain_Is_Found"
# )


@APP.route('/event/comment', methods=['GET'])
def event_comments():
    event_id = int(request.args.get('event_id'))
    comments = display_comments(event_id)
    return sendSuccess(comments)

@APP.route('/event/comment/post', methods=['POST'])
def comment_post():
    event_id = int(request.form.get('event_id'))
    print(request.form.get('token'))
    comment_dict = post_comment(request.form.get('token'), event_id,
                 request.form.get('message'))
    return sendSuccess(comment_dict)

@APP.route('/event/reply/post', methods=['POST'])
def reply_post():
    event_id = int(request.form.get('event_id'))
    comment_id = int(request.form.get('comment_id'))
    reply_dict = post_comment(request.form.get('token'), event_id, comment_id,
                 request.form.get('message'))
    return sendSuccess(reply_dict)

@APP.route('/user/update', methods=['POST'])
def update_info():
    phone_no = request.form.get('phone_no')
    username = request.form.get('username')
    update = modify_details(request.form.get('token'), username, phone_no)
    return sendSuccess (update)

@APP.route('/user/save', methods=['POST'])
def save_unsave_event():
    event_id = int(request.form.get('event_id'))
    update = event_save_unsave(request.form.get('token'), event_id)
    return sendSuccess (update)

@APP.route('/user/going', methods=['GET'])
def show_going():
    going = display_going(request.args.get('token'))
    return sendSuccess(going)

@APP.route('/user/follow', methods=['POST'])
def follow_artist():
    artist_id = int(request.form.get('artist_id'))
    follow = artist_follow_unfollow(request.form.get('token'), artist_id)
    return sendSuccess(follow)

@APP.route('/user/following', methods=['GET'])
def show_following():
    following = display_following(request.args.get('token'))
    return sendSuccess(following)

@APP.route('/user/event/recommend', methods=['GET'])
def recommend_events():
    rec = event_recommendations(request.args.get('token'))
    return sendSuccess(rec)

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000), debug=True)
    # APP.run(port=5009, debug=True)

