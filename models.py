"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Model for handling pet info"""

    __tablename__="pets"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True)

    name = db.Column(
        db.Text,
        nullable=False
    )

    species = db.Column(
        db.Text,
        nullable=False
    )

    photo_url = db.Column(
        db.Text,
        nullable=False
    )

    age = db.Column(
        db.Text,
        db.CheckConstraint("age IN ('baby', 'young', 'adult', 'senior')"),
        nullable=False
    )

    notes = db.Column(
        db.Text,
        nullable=False
    )

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )


