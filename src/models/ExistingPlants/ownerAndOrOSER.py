#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class OwnerAndOrOSER(db.Model):
    '''table des osers.'''

    __tablename__ = 'existing_plant_owner_and_or_oser'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom
    
    
    def isOwner() : 
        """message verification si l'instant est Propriétaire"""
        pass
    def isOSER() : 
        """message verification si l'instant est OSER"""
        pass

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_plant_owner_and_or_oser %r>' % self.name