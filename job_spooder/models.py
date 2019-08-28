from job_spooder import db
from datetime import datetime


class JobArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(80))
    href = db.Column(db.String(250))
    title = db.Column(db.String(250))
    description = db.Column(db.Text())
    company = db.Column(db.String(80))
    image = db.Column(db.String(250))
    city = db.Column(db.String(80))
    days_left = db.Column(db.String(80))
    created = db.Column(db.String(80))
    last_modified = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self):
        return '<{}: id {}>'.format(self.__class__.__name__, self.id)

    def as_dict(self):
        return {e.name: str(getattr(self, e.name)) for e in self.__table__.columns}
