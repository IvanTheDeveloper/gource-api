from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import all_blueprints
    for bp in all_blueprints:
        app.register_blueprint(bp)

    return app
