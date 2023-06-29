#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class PowerLineType(db.Model):
    '''table des type ligne électrique.'''

    __tablename__ = 'existing_powerLines_power_line_type'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_powerLines_power_line_type %r>' % self.wording