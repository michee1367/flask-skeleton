#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class EconomicActivityType(db.Model):
    '''table des type Activité économique.'''

    __tablename__ = 'local_economy_economic_activity_type'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<local_economy_economic_activity_type %r>' % self.wording  