from .env import env

config = {
    "DEBUG": env("DEBUG", cast=bool, default=True),
    "SQLALCHEMY_DATABASE_URI": "mysql+pymysql://user:password@127.0.0.1:3306/demo_db",
    "SQLALCHEMY_ECHO": False,
    "SQLALCHEMY_COMMIT_ON_TEARDOWN": True,
    "SQLALCHEMY_ENGINE_OPTIONS": {
        "pool_recycle": 1800,
        "pool_pre_ping": True,
    },
    "middlewares": [
        "{{cookiecutter.package_name}}.middleware.model.ModelMiddleware",
        "{{cookiecutter.package_name}}.middleware.panic.PanicMiddleware",
    ]
}
