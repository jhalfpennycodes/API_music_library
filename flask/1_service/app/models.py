from app import db


class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), unique=True, nullable=False)
    artist = db.Column(db.String(500), nullable=False)
    era = db.Column(db.String(500), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'artist': self.artist,
            'era': self.era
        }

