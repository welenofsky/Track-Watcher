#!/usr/bin/python3

import urllib.request
import json
import time


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


def get_last_track_history_time():
	track_history = None

	try:
		track_history = open('history.txt', 'r')
	except FileNotFoundError:
		try:
			track_history = open('history.txt', 'w+')
		except:
			print("Could not open track history file for writing\n")

	last_track_timestamp = track_history.read()

	if last_track_timestamp:
		return last_track_timestamp

	return None


def set_last_track_history_time(created_at):
	if created_at is None:
		return None

	track_history = None

	try:
		track_history = open('history.txt', 'w+')
	except:
		print("Could not open track history file for writing\n")

	track_history.write(created_at)

	return None


def get_last_track_datetime(tracks):
	if tracks is None:
		return None

	parsed_tracks = json.loads(tracks)

	if len(parsed_tracks) > 0:
		last_track = parsed_tracks[0]

	soundcloud_timestamp 	= last_track["created_at"]
	track_title 			= last_track["title"]

	if soundcloud_timestamp:
		try:
			current_track_created_at 	= time.strptime(soundcloud_timestamp, "%Y/%m/%d %H:%M:%S %z")
			last_track_created_at 		= get_last_track_history_time()

			if last_track_created_at:
				last_track_created_at = time.strptime(last_track_created_at, "%Y/%m/%d %H:%M:%S %z")
				if last_track_created_at <= current_track_created_at:
					print("No new tracks at this time")
					exit()
			print(repr(last_track_created_at))
			print(repr(current_track_created_at))
			print("NEW TRACK: " + track_title)
			set_last_track_history_time(soundcloud_timestamp)

		except ValueError as e:
			print("bad timestamp received from soundcloud, exiting...\nError: " + e)
			exit()

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
			get_last_track_datetime(tracks)
		else:
			print("Could not find any tracks")

main()