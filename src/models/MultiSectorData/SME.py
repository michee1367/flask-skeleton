#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class SME(db.Model):
    '''table des PME (incubateurs des PME).'''

    __tablename__ = 'multi_sector_data_s_m_e'
    
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # "Nom Etablissement de santé"
    estimatedConsumption = db.Column(db.Float, nullable=False)  # "Consommation estimée lorsqu’existante"

    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<multi_sector_data_s_m_e %r>' % self.wording