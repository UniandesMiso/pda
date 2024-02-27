from properties.config.db import db


class Ground(db.Model):
    __tablename__ = "ground"
    id = db.Column(db.String, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    status = db.Column(db.String)
    address = db.Column(db.String)
