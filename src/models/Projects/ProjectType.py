#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ProjectType(db.Model):
    '''table des Type du Projet (hydroélectrique, solaire, extension…)'''

    __tablename__ = 'projects_project_type'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<projects_project_type %r>' % self.wording  