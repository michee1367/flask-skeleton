from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from routes.auth import auth
from models.machine import db

from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    jwt = JWTManager(app)
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/machines')
app.register_blueprint(auth, url_prefix='/')
migrate = Migrate(app, db)  # Initializing the migration


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)