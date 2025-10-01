from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, makedirs

db = SQLAlchemy()
DB_NAME = "database.db"

BASEDIR = path.abspath(path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    DB_PATH = path.join(BASEDIR, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"

    # Initialize db with this app
    db.init_app(app)
    # Ensure database + tables exist
    create_database(app)

    # Register blueprint(s)
    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    return app
    
def create_database(app):
    """Create the SQLite database + tables if they don’t exist."""
    with app.app_context():
        from .models import Result   #Import models inside context
        db.create_all()              #This ensures the `result` table exists
        print("Database initialized and tables created")