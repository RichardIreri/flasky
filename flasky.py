""" Main script. """
# This is where the application instance is defined.

import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

# Creating an application context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

# Unittest launcher command
@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)