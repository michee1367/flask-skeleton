import click
from flask import Blueprint
import json
import pandas as pd
import numpy as np
from models.ExistingPlants.existingPlantType import ExistingPlantType
from models.ExistingPlants.existingPlant import ExistingPlants
from models import db


loadData = Blueprint('load-data', __name__)

@loadData.cli.command('load-existing-plant')
@click.argument('path')
def loadExistingPlants(path):
    """ load-existing-plant """
    with open(path) as f:
        jsonData = json.load(f)["features"]
        data = [it["properties"] for it in  jsonData]
        geometries = [it["geometry"] for it in jsonData ]
        #data = json.load(f).items()
        item = data[0]
        geometry = geometries[0]
        
        #insertExistingPlants(data=item,geometry=geometry)
        #print(item)
        #print(geometry)
        
        df = pd.DataFrame.from_dict(data)
        i,j = df.axes
        res = [insertExistingPlants(data[n],geometries[n])  for n in i.values]
        print(res)
        #df.iloc()

def insertExistingPlants(data, geometry) :
    """" insert data existing plants """
    # Nom, Source
    print("#Start")
    name = data["Nom"]
    typeName = data["Source"]
    if data["Puissance"] == "N/A" : 
        power = 0.0
    else :
        power = data["Puissance"]
    coordinates = geometry["coordinates"]
    
    geom = "SRID=4326;POINT("+ str(coordinates[0])  + " "+ str(coordinates[1])+")"
    print(geom)
    #print(data)
    
    
    type = insertExistingPlantsType(name=typeName)
    entity = ExistingPlants.query.filter_by(name=name, type_id=type.id).first()
    #print(entity)
    #return 0
    if entity is not None :
        print(entity)
        return 0
    
    #print(name)
    #return 
    entity = ExistingPlants()
    entity.name = name
    entity.power = power
    entity.props = data
    entity.geom = geom
    entity.type_id = type.id
    entity.type = type
    
    #print(entity.props)
    
    #return
    db.session.add(entity)
    db.session.commit()
    
    
    print("#End")
    
    return 1

def insertExistingPlantsType(name) :
    """ insertExistingPlantsType """
    #data = db.session.execute(db.select(ExistingPlantType).order_by(ExistingPlantType.id)).scalars()
    data = ExistingPlantType.query.filter_by(name=name).first()
    #print(data)
    #res = [it for it in data]
    
    #print(res)
    #exit()
    
    if data is not None :
        return data
    
    entity = ExistingPlantType(name=name)
    db.session.add(entity)
    db.session.commit()
    
    return  entity
    #entity
        
def me_stats(path) :
    """ load-existing-plant """
    with open(path) as f:
        data = [it["properties"] for it in json.load(f)["features"] ] 
        #data = json.load(f).items()
        item = data[0]
        df = pd.DataFrame.from_dict(data)
        i,j = df.axes
        maxs = [df[it].value_counts().max() for it in j.values]
        maxs = [it for it in df["Nom"].value_counts()]
        fid_12_0 = [df.loc[n].values for n in i.values if df.loc[n]["FID_12"] == 0]
        #df.iloc()
        table = pd.pivot_table(df, values='Nom', index='Source',
                       columns=[j.values[0]], aggfunc=len, fill_value=0)
        k = 4
        print(j.values[k])
        print(df[j.values[k]].value_counts())
        val = pd.DataFrame(fid_12_0)
        print( table )
        
        print( np.max([table[item].loc["Hydro"] + table[item].loc["PV"] + table[item].loc["Thermique"]   for item in table])  )