#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class TelecommunicationOperator(db.Model):
    '''table des opérateurs de communications.'''

    __tablename__ = 'telecommunication_operator_telecommunication'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<telecommunication_operator_telecommunication %r>' % self.name