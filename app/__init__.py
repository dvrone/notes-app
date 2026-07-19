from flask import Flask

import config


def create_app():
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        static_url_path="/",
    )
    app.config.from_object(config.Config)

    from app.routes import main

    app.register_blueprint(main.bp)

    return app
