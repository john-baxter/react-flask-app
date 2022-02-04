#from . import app

def deploy():
    """Run deployment Task."""
    from app import create_app,db
    from flask_migrate import update,migrate,init,stamp
    from models import Articles

    app = create_app()
    app.app_context().push()

    # creat database and tables
    db.create_all()

    # migrate database to latest revision
    stamp()
    migrate()
    upgrade()

deploy()
