#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()
from models import db

# Creating the Inserttable for inserting data into the database


class ProjectState(db.Model):
    '''table des État du projet  (non lancé, lancé, réceptionné provisoirement ou définitivement, concession attribuée )'''

    __tablename__ = 'projects_project_state'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    wording = db.Column(db.String(80), nullable=False) # nom
    
    # method used to represent a class's objects as a string
    def __repr__(self):
        return '<projects_project_state %r>' % self.wording  