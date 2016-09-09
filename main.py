#!/usr/bin/python3
import urllib.request


def get_tracks(user, client_id):
	api_endpoint 	= "http://api.soundcloud.com/users/:user/tracks?client_id=:client_id"
	api_endpoint 	= api_endpoint.replace(':user', user)
	api_endpoint 	= api_endpoint.replace(':client_id', client_id)
	page			= urllib.request.urlopen(api_endpoint)

	return page.read().decode('utf-8')

def main():
	secrets = None

	try:
		secrets = open('secrets.txt', 'r')
	except FileNotFoundError:
		print("Could not find secrets.txt, exiting")
		exit()


	if secrets:
		client_id 	= secrets.read()
		tracks 		= get_tracks('ytcracker', client_id)

		print(tracks)

main()