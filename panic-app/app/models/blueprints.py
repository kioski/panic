from sanic import Blueprint
from app.models.api import handle, getAll

bp = Blueprint('mongodb-api')

bp.add_route(handle, '/posts')
bp.add_route(getAll, '/getAll')


