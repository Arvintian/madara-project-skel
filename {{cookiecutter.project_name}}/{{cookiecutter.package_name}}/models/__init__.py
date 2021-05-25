from {{cookiecutter.package_name}}.config import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pretty_logging import pretty_logger

# database
engine = create_engine(config["SQLALCHEMY_DATABASE_URI"], echo=config["SQLALCHEMY_ECHO"], **config["SQLALCHEMY_ENGINE_OPTIONS"])
Session = sessionmaker(bind=engine)


class SessionContext(object):

    def __init__(self):
        self.session = None

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()
        if not exc_type is None:
            pretty_logger.error("{} {} {}".format(exc_type, exc_value, exc_tb))
