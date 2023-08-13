# Doc

## Require

- linux os
- python 3.8.10 in your machine 


## install the package

- sudo apt-get install libpq-dev
- sudo apt-get install python-dev-is-python3
- sudo apt-get install python3-wheel
- pip3 install wheel

## Init command

- Create vitual environement

```bash

    python3 -m venv venv

```


- Activate the vitual environement

```bash

    source venv/bin/activate

```

- create postgis extension
```
    open pgAdmin
    select (click) your database
    click "SQL" icon on the bar
    run "CREATE EXTENSION postgis;" code
```


- Install dependances

```bash

    python3 -m pip install -r requirements.txt

```


- Change directory

```bash

    cd src

```

- Initialize database

```bash

    flask db init 

```
- Generate migration

```bash

    flask db migrate 

```
- Upgrade database

```bash

    flask db upgrade 

```

- Load Data
```bash

 flask load-data load-existing-plant ../data/RDC_Centrales_existantes_GEOJSON.geojson

 flask load-data load-projects "../data/RDC_Centroides_RA_GEOJSON.geojson"  "../data/RDC_Rayons_d_action_GEOJSON.geojson"

```