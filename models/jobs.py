from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, nullable=False)
    uuid = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=True)
    status_val = db.Column(db.String(50), nullable=True)
    result = db.Column(db.String(500), nullable=True)
    startedAt = db.Column(db.DateTime, nullable=True)
    endedAt = db.Column(db.DateTime, nullable=True)
    errorLog = db.Column(db.String(1000), nullable=True)
    machineID = db.Column(db.Integer, ForeignKey('machine.id'), nullable=False)
    machine = db.relationship('Machine', backref='jobs')
