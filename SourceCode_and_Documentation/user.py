from db import *

def modify_details (token, firstname, lastname, phone_no, email):
    data = getData()
    user = getUserFromToken(token)
    if firstname == '':
        firstname = user['name_first']
    if lastname == '':
        lastname = user['name_last']
    if phone_no == '':
        phone_no = user['phone_no']
    if email == '':
        email = user['email']     
    if len(firstname) > 20 or len(lastname) > 20:
        raise ValueError_http("Name cannot be longer than 20 characters")
    if len(phone_no) != 10:
        raise ValueError_http("Invalid phone number")
    validEmail(email)
    user['name_first'] = firstname
    user['name_last'] = lastname
    user['phone_no'] = phone_no
    user['email'] = email
    
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