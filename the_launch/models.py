from datetime import datetime
from the_launch import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    phone_no = db.Column(db.String(10), nullable=True, default='')
    comments = db.relationship('Comment', backref='author', lazy=True)
    comment_replies = db.relationship('Reply', backref='author', lazy=True)
    # enquiries = db.relationship('Enquiries', backref='user', lazy=True)
    # im_going = db.relationship('ImGoing', backref='user', lazy=True)
    # following = db.relationship('UserFollowing', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone_no}', '{self.image_file}')"

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    events = db.relationship('Event', backref='artist', lazy=True)
    # followed_by = db.relationship('UserFollowing', backref='artist', lazy=True)

    def __repr__(self):
        return f"Artist('{self.name}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    comments = db.relationship('Comment', backref='event', lazy=True)
    # im_going = db.relationship('ImGoing', backref='event', lazy=True)

    def __repr__(self):
        return f"Event('{self.name}', '{self.date}')"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    replies = db.relationship('Reply', backref='comment', lazy=True)

    def __repr__(self):
        return f"Comment('{self.user_id}', '{self.date}', '{self.message}')"

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Reply'{self.user_id}', '{self.date}', '{self.message}')"

# class Enquiry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_opened = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     status_resolved = db.Column(db.Boolean, nullable=False, default=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     messages = db.relationship('EnquiryMessage', backref='enquiry', lazy=True)

#     def __repr__(self):
#         return f"Enquiry('{self.user_id}', '{self.date_opened}', '{self.status_resolved}')"

# class EnquiryMessage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     message = db.Column(db.Text, nullable=False)
#     enquiry_id = db.Column(db.Integer, db.ForeignKey('enquiry.id'), nullable=False)

#     def __repr__(self):
#         return f"Enquiry Message('{self.message}', '{self.date_sent}')"

# class ImGoing(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)

#     def __repr__(self):
#         return f"Im Going('{self.event_id}')"

# class UserFollowing(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

#     def __repr__(self):
#         return f"Following('{self.artist_id}')"

# class MusicGenre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

#     def __repr__(self):
#         return f"Following('{self.artist_id}')"