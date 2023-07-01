#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ProgressStatus(db.Model):
    '''table des Statut d’avancement (études, contractualisation, réalisation en cours – avec échéances associées lorsque disponibles)'''

    __tablename__ = 'projects_progress_status'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<projects_progress_status %r>' % self.wording  