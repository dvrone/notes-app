from datetime import datetime as dt

from flask_login import UserMixin

from app.extensions import db


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    joined_at = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} email={self.email}>"
