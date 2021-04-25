from {{cookiecutter.package_name}}.config import config
from {{cookiecutter.package_name}}.controllers import bp_api
from madara.app import Madara

app = Madara(config=config)

app.register_blueprint(bp_api, url_prefix='/api')
