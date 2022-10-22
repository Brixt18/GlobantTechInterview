import collections
import logging
import statistics as stats

import requests as r


def get_info() -> "list[dict]":
	berries = []

	url = "https://pokeapi.co/api/v2/berry/?limit=100"

	while url:
		try:
			resp = r.get(url).json()
			url = resp.get("next")

			for berrie in resp.get("results"):
				name = berrie["name"]

				info = r.get(berrie["url"]).json()

				berries.append(
					{
						"name": name,
						"growth_time": info["growth_time"]
					}
				)

		except Exception as e:
			logging.error("Error trying to get berries info")
			logging.error(e)

	return berries


def get_all_berries_stats() -> dict:
	berries = get_info()
	growth_times = [b["growth_time"] for b in berries]
	frequency = [
		{
			"growth_time": time,
			"frequency": freq
		} for time, freq in
         			dict(collections.Counter(growth_times)).items()
	]

	return {
		"berries_names": [b["name"] for b in berries],
		"min_growth_time": min(growth_times),
		"median_growth_time": stats.median(growth_times),
		"max_growth_time": max(growth_times),
		"variance_growth_time": round(stats.variance(growth_times), 2), #Data is rounded to 2 decimals to avoid large float numbers as 14.99374. That can be cosfusing.
		"mean_growth_time": round(stats.mean(growth_times), 2), # same as ^
		"frequency_growth_time": frequency,
	}
