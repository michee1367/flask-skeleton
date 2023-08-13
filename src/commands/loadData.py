import click
from flask import Blueprint
import json
import pandas as pd
import numpy as np
from models.ExistingPlants.existingPlantType import ExistingPlantType
from models.ExistingPlants.existingPlant import ExistingPlants
from models.Projects.Project import Project
from models.Projects.ProjectType import ProjectType
from models import db
import haversine as hs
from haversine import Unit
import math
loadData = Blueprint('load-data', __name__)
from sqlalchemy import func

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

@loadData.cli.command('load-projects')
@click.argument('pathpoints', nargs=1)
@click.argument('pathraduis', nargs=1)
def loadProjects(pathpoints, pathraduis):
    """ projects """
    #me_stats(pathpoints)
    #return
    with open(pathpoints) as fP:
        with open(pathraduis) as fR:
            jsonDataPoints = json.load(fP)["features"]
            jsonDataRaduis = json.load(fR)["features"]
            k = 10
            locList1 = jsonDataPoints[k]["geometry"]["coordinates"]
            locsRaduis = jsonDataRaduis[k]["geometry"]["coordinates"][0]
            locList2 = jsonDataRaduis[k]["geometry"]["coordinates"][0][0]
            
            locList3 = jsonDataRaduis[k]["geometry"]["coordinates"][0][300]
            countPoint = len(jsonDataRaduis[k]["geometry"])
            print(locList1)
            print(locList2 )
            print(locList3 )
            loc1= tuple(locList1)
            loc2= tuple(locList2)
            loc3= tuple(locList3)
            dists = [hs.haversine(loc1,tuple(locList), Unit.METERS)  for locList in  locsRaduis ]
            
            dist1 = hs.haversine(loc1,loc2, Unit.METERS)
            dist2 = hs.haversine(loc1,loc3, Unit.METERS)
            #print(dist1)
            #print(math.sqrt(np.var(dists)) )
            #print(np.mean(dists))
            #print(np.quantile(dists, 0.75))
            #print(np.max(dists))
            #print(np.max(dists) - np.min(dists))
            #print(jsonDataPoints)
            #return 
            
            transData =[
                insertProjects(dataRadius=jsonDataRaduis[idIt], data=it["properties"], geometry=it["geometry"]) 
                for idIt, it in enumerate(jsonDataPoints) 
            ]
            print(transData)
            return 


def insertProjects(data, dataRadius, geometry) :
    """" insert data project """
    # Nom, Source
    print("#Start")
    name = data["Nom"]
    typeName = data["Source"]
    
    if name is None :
        name = "Project_" + str(data["FID_1"])
    #print((dataRadius, data, geometry["coordinates"]))
    
    coordinates = geometry["coordinates"]
    
    locsRaduis = dataRadius["geometry"]["coordinates"][0]
    
    locCenter= tuple(coordinates)
    dists = [hs.haversine(locCenter,tuple(locList), Unit.METERS)  for locList in  locsRaduis ]
    #print(np.mean(dists) )
    radius = np.mean(dists)
    
    
    if data["Puissance"] == "N/A" : 
        power = 0.0
    else :
        power = data["Puissance"]
    
    #return 0
    #coordinates = geometry["coordinates"]
    
    geom = "SRID=4326;POINT("+ str(coordinates[0])  + " "+ str(coordinates[1])+")"
    print(geom)
    #print(data)
    #return 0
    if typeName is None :
        type = None
        entity = Project.query.filter_by(wording=name).first()
    else :
        type = insertProjectsType(name=typeName)
        #return 0
        entity = Project.query.filter_by(wording=name, type_id=type.id).first()
        
    print(entity)
    #return 0
    if entity is not None :
        print( db.session().scalar(entity.geomCentroid.ST_X()) )
        print( db.session().scalar(entity.geomCentroid.ST_Y()) )
        #print(entity.geomCentroid.ST_X() )
        
        return 0
    
    #print(name)
    #return 
    entity = Project()
    
    entity.wording = name
    entity.plannedPower = power
    entity.props = data
    entity.geomCentroid = geom
    if type is not None :
        entity.type_id = type.id
        entity.type = type
    entity.radius = radius
    
    #print(entity.props)
    
    #return
    db.session.add(entity)
    db.session.commit()
    
    
    print("#End")
    
    return 1

def insertProjectsType(name) :
    """ insertProjectsType """
    #data = db.session.execute(db.select(ExistingPlantType).order_by(ExistingPlantType.id)).scalars()
    data = ProjectType.query.filter_by(wording=name).first()
    #print(data)
    #res = [it for it in data]
    
    print(data)
    #exit()
    
    if data is not None :
        return data
    
    entity = ProjectType(wording=name)
    #entity.wording
    db.session.add(entity)
    db.session.commit()
    
    return  entity
    #entity
        



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
        #fid_12_0 = [df.loc[n].values for n in i.values if df.loc[n]["FID_12"] == 0]
        #df.iloc()
        table = pd.pivot_table(df, values='Nom', index='Source',
                       columns=[j.values[0]], aggfunc=len, fill_value=0)
        k = 4
        print(j.values[k])
        print(df[j.values[k]].value_counts())
        #val = pd.DataFrame(fid_12_0)
        print( table )
        
        print( np.max([table[item].loc["Extension"] + table[item].loc["Hydroelectrique"] + table[item].loc["Photovoltaique"]   for item in table])  )