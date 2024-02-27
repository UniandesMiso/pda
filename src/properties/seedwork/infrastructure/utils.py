from os import environ, path
from time import time


def time_millis():
    return int(time() * 1000)


def get_pulsar_url():
    host = environ.get("BROKER_HOST", "localhost")
    port = environ.get("BROKER_PORT", "6650")
    return f"pulsar://{host}:{port}"


def get_database_url():
    return (
        "postgresql+psycopg2://"
        + f"{environ.get('DB_USER')}:{environ.get('DB_PASS')}@"
        + f"{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/"
        + f"{environ.get('DB_NAME')}"
    )
