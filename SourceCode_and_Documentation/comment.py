from db import *

comment_id = 0

def display_comments(event_id):
    data = getData()
    event = getEventFromEventId(event_id)
    comments = event['comments']
    return {
        'comments' : comments
    }

def post_comment(token, event_id, message):
    global comment_id

    if len(message) > 1000:
        raise ValueError_http("Message cannot be longer than 1000 characters")
    print(token)
    # add comment details
    event = getEventDetails(event_id)
    comment_id += 1
    event['comments'].insert(0, {
        'id': comment_id,
        'author': getUidFromToken(token),
        'message': message,
        'time_posted': str(datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()),     #convert to sydney timezone
        'replies' : []
    })
    return {'comment_id': comment_id}

def reply_comment(token, event_id, comment_id, message):

    if len(message) > 1000:
        raise ValueError_http("Message cannot be longer than 1000 characters")

    # add reply details
    comment = getCommentDetails(event_id, comment_id)
    comment['replies'].insert(0, {
        'u_id': getUidFromToken(token),
        'message': message,
        'time_posted': str(datetime.datetime.now(datetime.timezone.utc).astimezone().timestamp()),     #convert to sydney timezone
    })

# def message_remove(token, comment_id):
#     # message doesnt exist
#     if commentExists(comment_id) is False:
#         raise ValueError_http('Comment does not exist')
#     event_id = findComment(comment_id)['event_id']
#     # user must be authorized
#     if comment_belong_to_user(token, comment_id):
#         event = findComment(comment_id)
#         event['comment'].remove(getCommentInfo(comment_id))
#     else:
#         raise AccessError('User not authorized to remove message')

