from os import environ
from threading import Thread
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from contracts.config import config
from contracts.config.db import init_db
from contracts.api.sales import bp as sales_bp

import contracts.modules.sales.infrastructure.consumers as sales_consumer


def create_app():
    config_name = environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_error_handler(HTTPException, exception_handler)

    init_db(app)
    init_api(app)
    init_consumers(app)

    return app


def init_api(app):
    app.register_blueprint(sales_bp)


def init_consumers(app):
    Thread(target=sales_consumer.subscribe_2_events, args=[app]).start()


def exception_handler(ex: HTTPException):
    return jsonify({"message": ex.description}), ex.code
