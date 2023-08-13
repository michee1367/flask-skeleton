#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class TerritoryDemand(db.Model):
    '''table des demandes.'''

    __tablename__ = 'territory_demand'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False) # année
    men = db.Column(db.Float, nullable=False) # Ménages à électrifier
    dem = db.Column(db.Float, nullable=False) # Demande des ménages [MWh]
    dem_ter = db.Column(db.Float, nullable=False) # Demande du secteur tertaire [MWh]

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<territory_demande %r>' % self.year