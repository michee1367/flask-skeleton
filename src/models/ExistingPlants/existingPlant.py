#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db
from geoalchemy2.types import Geometry
from models.ExistingPlants.existingPlantType import ExistingPlantType

from sqlalchemy.dialects import postgresql

# Creating the Inserttable for inserting data into the database


class ExistingPlants(db.Model):
    '''table des secteurs.'''

    __tablename__ = 'existing_plant_existing_plant'
    postgresql.JSON
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # nom
    power = db.Column(db.Float, nullable=False)  # "Puissance installée/ disponible [KW]"
    nbrOfhouseholds = db.Column(db.Integer, nullable=True) # "Nombre de ménages connectés"
    powerForProductiveUsed = db.Column(db.Float, nullable=True) # "Puissance ménages [KW]"
    powerForProductiveUsed = db.Column(db.Float, nullable=True) # "Puissance usage productif/ industriel"
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326)) # geom point
    props = db.Column(postgresql.JSON) # other property
    
    type_id = db.Column(db.Integer, db.ForeignKey('existing_plant_existing_plant_type.id'))
    type = db.relationship("ExistingPlantType")

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<existing_plant_existing_plant %r>' % self.name
    
    
{ 
 "FID_1": 0, 
 "FID_12": 119, 
 "FID_1_1": 0, 
 "N°": 0, 
 "Nom": "Mbankana", 
 "Rivière": "Lufimi", 
 "Province": "KINSHASA", 
 "Territoire": "Maluku", 
 "Débit__m3": 0.0, 
 "Concession": None, 
 "Gestion": "Privé", 
 "Service": "S", 
 "Source": "Hydro",
 "Mise_en_se": 2015, 
 "Puissance": "0.05", 
 "Puissanc_1": None, 
 "Centre_c": "Mbankana", 
 "Long": 16.202558, 
 "Lat": -4.455346, 
 "FID_2": 0, 
 "TYPE": None, 
 "CODE_INS": 0, 
 "SURFACE": 0.0, 
 "TERRIT": "Maluku", 
 "POINT_X": 1803462.8169499997, 
 "POINT_Y": -493108.33437400003, 
 "P": 0.05, 
 "FID_3": 0, 
 "SCE_SEM": "INS", 
 "SCE_GEO": "UNDP/OCHA", 
 "MODIF": 1430179200000.0, 
 "ORIGINE": "Numerisation Saint Moulin / Image satellite", 
 "NOM_1": "Kinshasa", 
 "CODE_INS_1": 10, 
 "SURFACE_1": 10584.151287000001, 
 "CHEF_LIEU": "Kinshasa", 
 "Agence": None, 
 "Pool_ANSER": "Grand_Ouest" 
}