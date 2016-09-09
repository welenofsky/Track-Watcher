#!/usr/bin/python3

import urllib.request
import json
import time


def get_tracks(user, client_id):
    endpoint = "http://api.soundcloud.com/users/{user}/tracks?client_id={id}"
    endpoint = endpoint.format(user=user, id=client_id)

    try:
        page = urllib.request.urlopen(endpoint, timeout=5)
    except urllib.URLError as e:
        print("Could not connet to soundcloud, error: " + e)
        return None

    content = page.read()
    page.close()

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
    track_history.close()

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
    track_history.close()

    return None


def get_last_track_datetime(tracks):
    if tracks is None:
        return None

    parsed_tracks = json.loads(tracks)

    if len(parsed_tracks) > 0:
        last_track = parsed_tracks[0]

    soundcloud_timestamp = last_track["created_at"]
    track_title = last_track["title"]
    permalink = last_track["permalink_url"]

    if soundcloud_timestamp:
        try:
            current_track_created_at = time.strptime(soundcloud_timestamp,
                                                     "%Y/%m/%d %H:%M:%S %z")
            last_track_created_at = get_last_track_history_time()

            if last_track_created_at:
                last_track_created_at = time.strptime(last_track_created_at,
                                                      "%Y/%m/%d %H:%M:%S %z")
                if last_track_created_at <= current_track_created_at:
                    print("No new tracks at this time")
                    exit()
            print("NEW TRACK: " + track_title + "\nLINK: " + permalink)
            set_last_track_history_time(soundcloud_timestamp)

        except ValueError as e:
            print("bad timestamp received from soundcloud, exiting...\n" +
                  "Error: " + e)
            exit()


def main():
    secrets = None

    try:
        secrets = open("secrets.txt", "r")
    except FileNotFoundError:
        print("Could not find secrets.txt, exiting")
        exit()

    if secrets:
        client_id = secrets.read()
        tracks = get_tracks("ytcracker", client_id)

        secrets.close()

        if tracks:
            get_last_track_datetime(tracks)
        else:
            print("Could not find any tracks")

main()
