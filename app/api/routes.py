from app.utils.stats import get_all_berries_stats
from flask import make_response

from . import api_bp as bp


@bp.route("/allBerryStats/", methods=["GET"])
def all_berry_stats():
	resp = make_response(get_all_berries_stats(), 200)
	resp.headers["Content-Type"] = "application/json"

	return resp
