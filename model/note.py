from model import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(60), nullable=False)
    notebook_id = db.Column(db.Integer, db.ForeignKey("notebook.id"), nullable=False)
    notebook = db.relationship("Notebook", back_populates="notes")
