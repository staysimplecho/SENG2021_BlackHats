from db import *

def modify_details (token, username, phone_no, name):
    data = getData()
    user = getUserFromToken(token)
    if len(username) > 20:
        raise ValueError_http("Username cannot be longer than 20 characters")
    if len(phone_no) != 10:
        raise ValueError_http("Invalid phone number")
    if username == '':
        username = user['username']
    if phone_no == '':
        phone_no = user['phone_no']
    user['username'] = username
    user['phone_no'] = phone_no

    return (user)

def event_save_unsave (token, event_id):
    data = getData()
    user = getUserFromToken(token)
    if event_id in user['saved_events']:
        user['saved_events'].remove(event_id)
    else:
        user['saved_events'].append(event_id)
    return user['saved_events']

def display_going (token):
    data = getData()
    user = getUserFromToken(token)
    going = []
    for event_id in user['saved_events']:
        event = getEventFromEventId(event_id)
        details = {
            'event_id' : event['id'],
            'event' : event['name'],
            'date' : event['date']
        }
        going.append(details)
    return going

def artist_follow_unfollow (token, artist_id):
    data = getData()
    user = getUserFromToken(token)
    if artist_id not in user['following']:
        user['following'].append(artist_id)
    else:
        user['following'].remove(artist_id)
    return user['following']

def display_following (token):
    data = getData()
    user = getUserFromToken(token)
    following = []
    for artist_id in user['following']:
        artist = getArtistFromArtistId(artist_id)
        details = {
            'artist_id' : artist['id'],
            'name' : artist['name']
        }
        following.append(details)
    return following

def event_recommendations (token):
    data = getData()
    user = getUserFromToken(token)
    rec = []
    for artist_id in user['following']:
        artist = getArtistFromArtistId(artist_id)
        for event_id in artist['event_list']:
            artist_event = getEventFromEventId(event_id)
            rec.append(artist_event)
    for event in data['events']:
        if event['genre_id'] in user['interested_genre'] and event not in rec:
            rec.append(event)
    return rec