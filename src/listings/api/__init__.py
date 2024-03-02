from os import environ
from threading import Thread
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from listings.config import config
from listings.config.db import init_db
from listings.api.listings import bp as listings_bp

import listings.modules.listings.infrastructure.consumers as sales_consumer


def create_app():
    config_name = environ.get("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.register_error_handler(HTTPException, exception_handler)

    init_db(app)
    init_api(app)
    init_consumers()

    return app


def init_api(app):
    app.register_blueprint(listings_bp)


def init_consumers():
    Thread(target=sales_consumer.subscribe_2_events).start()


def exception_handler(ex: HTTPException):
    return jsonify({"message": ex.description}), ex.code
