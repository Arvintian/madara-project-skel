from madara.wrappers import Request
from madara.blueprints import Blueprint

bp_api = Blueprint("bp_api")


@bp_api.route("/echo", methods=["GET"])
def get_echo(request: Request):

    return {
        "code": 200,
        "result": "I am ok."
    }
