from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scripts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
