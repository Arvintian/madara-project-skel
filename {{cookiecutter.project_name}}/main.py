from {{cookiecutter.package_name}} import app
from gunicorn.app.base import BaseApplication
from pretty_logging import pretty_logger
import multiprocessing
import signal
import sys


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


def start_server():
    """
    启动 http server
    """
    def _start_server():
        pretty_logger.info("start server process")
        options = {
            "bind": "{}:{}".format("0.0.0.0", "5000"),
            "workers": 2,
            "accesslog": "-",
            "errorlog": "-",
        }
        WebApplication(app, options).run()
        return
    process = multiprocessing.Process(target=_start_server)
    process.daemon = False
    process.start()
    return process


def main():

    targets = [start_server]
    processes = []
    for target in targets:
        process = target()

    def exit_kill(sig, frame):
        if sys.version_info >= (3, 7):
            for proc in processes:
                proc.kill()
        else:
            for proc in processes:
                proc.terminate()
    for sig in [signal.SIGINT, signal.SIGHUP, signal.SIGTERM]:
        signal.signal(sig, exit_kill)
    signal.pause()


if __name__ == "__main__":
    main()
