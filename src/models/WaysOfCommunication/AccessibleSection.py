#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class AccessibleSection(db.Model):
    '''table Revêtement de la route (latéritique, sablonneux, bitume, béton).'''

    __tablename__ = 'ways_of_communication_accessible_section'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<ways_of_communication_accessible_section %r>' % self.wording