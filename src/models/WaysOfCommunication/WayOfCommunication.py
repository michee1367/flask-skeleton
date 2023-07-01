#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class WaysOfCommunication(db.Model):
    '''table Voies de communication.'''

    __tablename__ = 'ways_of_communication_ways_of_communication'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    length = db.Column(db.Float, nullable=False)  # "Longueur Voies de communication"
    tonnage = db.Column(db.Float, nullable=False)  # "Tonnage"
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<ways_of_communication_ways_of_communication %r>' % self.name