#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class MobileSubscriberBase(db.Model):
    '''table Parc des abonnés mobiles.'''

    __tablename__ = 'telecommunication_operator_mobile_subscriber_base'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<telecommunication_operator_mobile_subscriber_base %r>' % self.name