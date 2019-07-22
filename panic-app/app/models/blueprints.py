from sanic import Blueprint
from app.models.api import handle

bp = Blueprint('mongodb-api')
bp.add_route(handle, '/posts')


