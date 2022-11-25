#!env python

import os
import requests
import sys
import zipfile


def parse_args():
	args_n = len(sys.argv)

	if args_n < 3:
		sys.exit("Please provide username and repo name")

	user, repo = sys.argv[1], sys.argv[2]
	dest = sys.argv[3] if args_n > 3 else None

	return user, repo, dest


def parse_env():
	try:
		return os.environ["GH_TOKEN"]
	except KeyError:
		sys.exit("Please provide a GitHub token")


def download_latest_artefact(token, user, repo, dest=None):
	# Get a link for all artefacts
	artefacts_uri = f"https://api.github.com/repos/{user}/{repo}/actions/artifacts"
	artefacts = requests.get(artefacts_uri).json()

	# Crash if there is no repository or no artefacts
	try:
		if artefacts["total_count"] < 1:
			sys.exit(f"Repo {user}/{repo} doesn't have any artefacts")
	except KeyError:
		sys.exit(f"Couldn't retrieve repository artefacts. Please check if repo {user}/{repo} exists")

	# Request the latest artefact
	file_uri = artefacts["artifacts"][0]["archive_download_url"]
	zip_res = requests.get(file_uri, auth=requests.auth.HTTPBasicAuth("token", token))

	# Use the filename used for the artefact on GH as the default path
	if dest is None:
		dest = artefacts["artifacts"][0]["name"] + ".zip"

	# Save file
	with open(dest, "wb") as f:
		f.write(zip_res.content)

	# Test if GH replied with an actual ZIP file, and not an error JSON
	try:
		zipfile.ZipFile(dest)
		print(f"{dest} successfully downloaded")
	except zipfile.BadZipFile:
		print("Please check the correctness of provided token")
		os.remove(dest)


user, repo, dest = parse_args()
token = parse_env()
download_latest_artefact(token, user, repo, dest)
