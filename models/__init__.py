# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

# Import your models
from .machines import Machine  # Corrected import statement
from .scripts import Scripts
from .jobs import Job  # Corrected import statement
