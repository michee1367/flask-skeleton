from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
#@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)