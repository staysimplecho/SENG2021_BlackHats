import pickle
from json import dumps
import jwt, pickle, os, threading, datetime, random
from Error import AccessError, ValueError_http
import re

# import datetime

'''
'artists' : [{
    'id' : 1,
    'name' : 'Rihanna',
    'description' : 'Blah Blah .... ',
    'event_list' : [list of event ids ...],
    'genre_id' : 1
}]

'events' : [{
    'id' : 2,
    'name' : '',
    'date' : datetime,
    'ticket_avail' : true,
    'description' : 'blah blah blah .....',
    'location' : 'Metro Theatre, Sydney, NSW' 
    'artist' : 1 (artist_id)

}]

'''

data = {
    'artists': [{
        'id' : 1,
        'name' : 'The Morrisons',
        'description' : '',
        'event_list' : [1]
    }, {
        'id' : 2,
        'name' : 'Triple One',
        'description' : '',
        'event_list' : [2]
    }, {
        'id' : 3,
        'name' : 'Laura Ingram',
        'description' : '',
        'event_list' : [3]
    }],
    'events' : [{
        'id' : 1,
        'name' : 'The Morrisons',
        'date' : '2020-06-04',
        'ticket_avail' : True,
        'description' : '',
        'location' : 'City Recital Hall, Sydney, NSW, Australia',
        'artist' : 1,
        'comments' : [],
        'genre_id' : 1
    }, {
        'id' : 2,
        'name' : 'Triple One',
        'date' : '2020-06-06',
        'ticket_avail' : True,
        'description' : '',
        'location' : 'Metro Theatre, Sydney, NSW, Australia',
        'artist' : 2,
        'comments' : [],
        'genre_id' : 3
    }, {
        'id' : 3,
        'name' : 'Laura Ingram',
        'date' : '2020-05-02',
        'ticket_avail' : True,
        'description' : '',
        'location' : 'The Newsagency, Annandale, NSW, Australia',
        'artist' : 3,
        'comments' : [],
        'genre_id' : 5
    }],
    'users' : [{
        'id' : 1,
        'token' : 'token123',
        'name_first' : 'Sam',
        'name_last' : 'Parker',
        'password' : 'temppassword123',
        'phone_no' : '0412345678',
        'email' : 'sam@gmail.com',
        'saved_events' : [1, 2],
        'following' : [],
        'interested_genre' : [3, 5]
        
    }],
    'genres' : [{
        'id' : 1,
        'name' : 'Pop'
    }, {
        'id' : 2,
        'name' : 'Rock'
    }, {
        'id' : 3,
        'name' : 'Hip Hop'
    }, {
        'id' : 4,
        'name' : 'Jazz'
    }, {
        'id' : 5,
        'name' : 'Electronic'
    }]
}

# # Store data (serialize)
# with open('db.pickle', 'wb') as handle:
#     pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# # # Load data (deserialize)
# # with open('db.pickle', 'rb') as handle:
# #     unserialized_data = pickle.load(handle)

# # print(data == unserialized_data)
# # # print(unserialized_data)


def generateUid():
    data = getData()
    randomNum = random.randint(10000,99999)
    for user in data['users']:
        if randomNum == user['id']:
            generateUid()
    return randomNum

def getUserByEmail(email):
    global data
    for user in data["users"]:
        if user["email"] == email:
            return user
    raise ValueError_http("Email not found")

def userExists(email):
    global data
    for user in data["users"]:
        if user["email"] == email:
            return True
    return False

def getData():
    global data
    return data

def sendSuccess(data):
    return dumps(data)


def sendError(message):
    return dumps({
        '_error' : message,
    })

####################################
def getUidFromToken(token):
    global data
    for user in data['users']:
        if token == user['token']:
            return user['id']
    # print(token)
    raise ValueError_http("u_id not found")

def getUserFromToken(token):
    data = getData()
    for user in data['users']:
        if token == user['token']:
            return user
    raise ValueError_http("Invalid token")

####################################
def getEventDetails(event_id):
    data = getData()
    for event in data['events']:
        if event['id'] == event_id:
            return event
    raise ValueError_http('Event not found')

####################################
def getCommentDetails(event_id, comment_id):
    data = getData()
    event = getEventDetails(event_id)
    for commment in event['comments']:
        if comment['id'] == comment_id:
            return comment
    raise ValueError_http('Comment not found')

# def tokenize(email):
#     return str(jwt.encode({'email': email}, SECRET, algorithm='HS256'))

####################################
def getEventFromEventId(event_id):
    data = getData()
    for event in data['events']:
        if event['id'] == event_id:
            return event
    raise ValueError_http("Invalid event ID")

def getArtistFromArtistId(artist_id):
    data = getData()
    for artist in data['artists']:
        if artist['id'] == artist_id:
            return artist
    raise ValueError_http("Invalid artist ID")

def validEmail(email):
    data = getData()
    # need to include check for space
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email) or " " in email:
        raise ValueError_http("Invalid email")
    return True

# def reset_resetCode(email):
#     for dicts in data['resetCode']:
#         if dicts['email'] == email:
#             data['resetCode'].remove(dicts)

# def getUserById(u_id):
#     data = getData()
#     for i in data['users']:
#         if i['u_id'] == u_id:
#             return i
#     raise ValueError_http('User not found')

# def findResetcodeMatch(reset_code):
#     data = getData()
#     for dicts in data['resetCode']:
#         if dicts['reset_code'] == reset_code:
#             return dicts['email']
#     raise ValueError_http("Invalid reset_code") 

def reset_data():
    global data 
    data = {
    'users': [],
    'resetCode' : [],
    'channel' : [],
    }
    return data

# def getDictFromResetCode(reset_code):
#     data = getData()
#     for dicts in data['resetCode']:
#         if dicts['reset_code'] == reset_code:
#             return dicts
#     raise ValueError_http("Reset_code not found")
