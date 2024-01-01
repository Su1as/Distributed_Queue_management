from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
