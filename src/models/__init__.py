import os, glob
from flask_sqlalchemy import SQLAlchemy
from tools.packages import alls

db = SQLAlchemy()

#__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
__all__ = alls(__file__)

#print(__all__)

from models.machine import Inserttable