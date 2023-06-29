#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class EducationInstitutionCategory(db.Model):
    '''table des categories institution d'édication.'''

    __tablename__ = 'education_education_institution_category'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False) # "Nom de la categorie"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<education_education_institution_category %r>' % self.name