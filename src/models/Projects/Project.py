#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db
from geoalchemy2.types import Geometry
from models.Projects.ProjectType import ProjectType

from sqlalchemy.dialects import postgresql

# Creating the Inserttable for inserting data into the database


class Project(db.Model):
    '''table des projects'''

    __tablename__ = 'projects_project'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    plannedPower = db.Column(db.Float, nullable=True)  # "Puissance planifiée pour ménages [KW]"
    plannedPowerForHouseholds = db.Column(db.Float, nullable=True)  # "Puissance planifiée pour ménages [KW]"
    plannedPowerForProductive = db.Column(db.Float, nullable=True)  # "Puissance planifiée pour usage productif/ industriel [KW]"
    nbrHouseholds = db.Column(db.Integer, nullable=True)  # "nombre de ménages connectés"
    geomCentroid = db.Column(Geometry(geometry_type='POINT', srid=4326)) # geom point
    radius = db.Column(db.Float, nullable=False) # geom Polygon
    props = db.Column(postgresql.JSON) # other properties
    dataRadius = db.Column(postgresql.JSON) # other les données des rayons d'accès
    
    type_id = db.Column(db.Integer, db.ForeignKey('projects_project_type.id'))
    type = db.relationship("ProjectType")
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<projects_project %r>' % self.wording  