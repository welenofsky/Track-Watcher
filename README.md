# What is this
I made this to check for new tracks from an artist on soundcloud and let you know if there are new tracks

## Requirements
You need to make an app and get a Client ID from soundcloud.    
https://developers.soundcloud.com/

Once you acquire one put it in a file called **secrets.txt** in the root of the folder.

## Usage
```
usage: main.py [-h] [--t TIMEOUT] ARTIST

Choose an artist to monitor new tracks of.

positional arguments:
  ARTIST       The name or ID of the artist you want to track.

optional arguments:
  -h, --help   show this help message and exit
  --t TIMEOUT  How long to wait for soundcloud API to respond in seconds.
```
  
## Example
```
python main.py zackdelarocha
NEW TRACK: digging for windows
LINK: http://soundcloud.com/zackdelarocha/digging-for-windows
```
