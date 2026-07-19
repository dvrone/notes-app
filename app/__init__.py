from flask import Flask

import config
from app import extensions as ext


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.config.from_object(config.Config)

    # initialize extensions
    ext.db.init_app(app)
    # ext.login_manager.init_app(app)
    ext.csrf.init_app(app)

    from app.routes import main

    app.register_blueprint(main.bp)

    return app
