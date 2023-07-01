#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class RoadSurface(db.Model):
    '''table Tronçon accessible ou fonctionnel.'''

    __tablename__ = 'ways_of_communication_mode_of_transport'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<ways_of_communication_mode_of_transport %r>' % self.wording