#!/usr/bin/python3

import urllib.request


def get_tracks(user, client_id):
	api_endpoint = "http://api.soundcloud.com/users/{user}/tracks?client_id={client_id}"
	api_endpoint = api_endpoint.format(
		user		= user,
		client_id	= client_id
	)

	try:
		page = urllib.request.urlopen(api_endpoint)
	except URLError as e:
		print("Could not connet to soundcloud, error: " + e)
		return None

	content = page.read()

	if content is None:
		return None

	return content.decode("utf-8")


def main():
	secrets = None

	try:
		secrets = open("secrets.txt", "r")
	except FileNotFoundError:
		print("Could not find secrets.txt, exiting")
		exit()


	if secrets:
		client_id 	= secrets.read()
		tracks 		= get_tracks("ytcracker", client_id)

		if tracks:
			print(tracks)
		else:
			print("Could not find any tracks")

main()