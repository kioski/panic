from sanic_script import Manager
from app.commands.runserver import RunServerCommand
from app import app

manager = Manager(app)
manager.add_command('run', RunServerCommand)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
