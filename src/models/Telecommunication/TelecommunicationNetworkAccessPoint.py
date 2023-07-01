#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class TelecommunicationNetworkAccessPoint(db.Model):
    '''table des points d'accès réseau.'''

    __tablename__ = 'telecommunication_operator_telecommunication_network_access_point'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephoneNetworkQuality = db.Column(db.String(80), nullable=False) # qualité d'appel
    telephoneNetworkQuality = db.Column(db.String(80), nullable=False) # qualité internet
    estimatedConsumption = db.Column(db.Float, nullable=False)  # "Consommation estimée lorsqu’existante"
    
    
    def hasAccessToInternetServices() :
        """Message pour demander s'il y a Données géographique accès aux services Internet"""
        pass
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<telecommunication_operator_telecommunication_network_access_point %r>' % self.name