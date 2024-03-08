from os import environ
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
        + f"{environ.get('DB_USER', 'postgres')}:{environ.get('DB_PASS', 'postgres')}@"
        + f"{environ.get('DB_HOST', 'localhost')}:{environ.get('DB_PORT', '5432')}/"
        + f"{environ.get('DB_NAME', 'pda')}"
    )
