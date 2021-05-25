from {{cookiecutter.package_name}} import app
from gunicorn.app.base import BaseApplication


class WebApplication(BaseApplication):

    def __init__(self, application, options=None):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load_config(self):
        the_config = {key: value for key, value in self.options.items()
                      if key in self.cfg.settings and value is not None}
        for key, value in the_config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


def main():

    options = {
        "bind": "{}:{}".format("0.0.0.0", "5000"),
        "workers": 2,
        "accesslog": "-",
        "errorlog": "-",
    }

    WebApplication(app, options).run()


if __name__ == "__main__":
    main()
