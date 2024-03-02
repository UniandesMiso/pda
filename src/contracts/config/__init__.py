from os import environ


class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://"
        + f"{environ.get('DB_USER', 'postgres')}:{environ.get('DB_PASS', 'postgres')}@"
        + f"{environ.get('DB_HOST', 'localhost')}:{environ.get('DB_PORT', '5432')}/"
        + f"{environ.get('DB_NAME', 'pda')}"
    )


class DevelopmentConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
