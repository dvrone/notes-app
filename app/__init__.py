from flask import Flask

import config
from app import extensions as ext
from app.models import User
from app.routes import auth, main


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
    ext.login_manager.init_app(app)
    ext.csrf.init_app(app)

    # login manager configurations
    ext.login_manager.login_message = "Welcome back!"
    ext.login_manager.login_message_category = "info"
    # ext.login_manager.login_view = ""

    # register blueprints
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    # set user loader
    @ext.login_manager.user_loader
    def load_user(user_id: int):
        return User.query.get(user_id)

    return app
