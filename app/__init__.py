from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루 프린트
    from .views import main, Question, Answer, Auth
    app.register_blueprint(main.bp)
    app.register_blueprint(Question.bp)
    app.register_blueprint(Answer.bp)
    app.register_blueprint(Auth.bp)

    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
