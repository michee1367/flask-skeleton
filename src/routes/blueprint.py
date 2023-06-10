from flask import Blueprint
from controllers.machineController import index, create, insert, all

from flask_jwt_extended import jwt_required

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/', methods=['GET'])
@jwt_required()
def indexWrapper() :
    return index()

blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/all', methods=['GET'])(all)
