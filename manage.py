# manage.py

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from application import app, db

# Initialize Flask-Script
manager = Manager(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Add the Migrate command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
