#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class Project(db.Model):
    '''table des projects'''

    __tablename__ = 'projects_project'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    plannedPowerForHouseholds = db.Column(db.Float, nullable=False)  # "Puissance planifiée pour ménages [KW]"
    plannedPowerForProductive = db.Column(db.Float, nullable=False)  # "Puissance planifiée pour usage productif/ industriel [KW]"
    nbrHouseholds = db.Column(db.Integer, nullable=False)  # "nombre de ménages connectés"
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<projects_project %r>' % self.wording  