#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class PowerLine(db.Model):
    '''table des ligne électrique.'''

    __tablename__ = 'existing_powerLines_power_line'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom
    tension = db.Column(db.Float, nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_powerLines_power_line %r>' % self.name