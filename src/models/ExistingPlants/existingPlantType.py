#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ExistingPlantType(db.Model):
    '''table des secteurs.'''

    __tablename__ = 'existing_plant_existing_plant_type'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_plant_existing_plant %r>' % self.name