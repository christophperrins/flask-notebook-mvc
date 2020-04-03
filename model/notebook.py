from model import db

class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    notes = db.relationship("Note", back_populates="notebook")