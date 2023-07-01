#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ModeOfTransport(db.Model):
    '''table Voies Mode de transport ou véhicules d’usage (navigabilité, voiture et type
de voiture, train, baleinière, avion…).'''

    __tablename__ = 'ways_of_communication_mode_of_transport'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<ways_of_communication_mode_of_transport %r>' % self.name