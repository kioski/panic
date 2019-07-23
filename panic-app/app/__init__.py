from sanic import Sanic
from sanic_mongodb_ext import MongoDbExtension
from umongo import MotorAsyncIOInstance

from app.models.blueprints import bp as mongodb_bp

app = Sanic("Panic-API-whatevers")
#app.config.from_envvar('APP_CONFIG_PATH')
# config
app.config.update({
    'MONGODB_DATABASE': 'dbhaxspace',
    'MONGODB_URI': 'mongodb://dev1:version1@ds035448.mlab.com:35448/dbhaxspace',
    'LAZY_UMONGO': MotorAsyncIOInstance()
})

app.mongodb = MongoDbExtension(app)

app.blueprint(mongodb_bp)
