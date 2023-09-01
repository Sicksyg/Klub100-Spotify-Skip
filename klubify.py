import subprocess
import sys
from time import time, sleep
import json

try:
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'spotipy'])
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth


scope = "user-library-read"


with open("./settings.json", "r") as fp:
    settings = json.load(fp)

print(settings)

deviceid = settings["deviceid"]
cid = settings["cid"]
secret = settings["secret"]
uri = "http://localhost:8080/callback/"
scpe = "user-modify-playback-state"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri= uri, scope= scpe))
sp.start_playback(device_id=deviceid)
songcount = 2


#-----------------------------------------------------------------------------

print(r"""
 _    _ _      _     _ ______      __  ______  ______ 
| |  / ) |    | |   | (____  \    /  |/ __   |/ __   |
| | / /| |    | |   | |____)  )  /_/ | | //| | | //| |
| |< < | |    | |   | |  __  (     | | |// | | |// | |
| | \ \| |____| |___| | |__)  )    | |  /__| |  /__| |
|_|  \_)_______)______|______/     |_|\_____/ \_____/ 
                                                      """)
print("Song: 1  -----> DRIK!!")

"""Main running time code"""

while True:
    sleep(60) #wait to be executed

    #sp.user_follow_artists()
    sp.next_track(device_id= deviceid)

    print("Song: " + str(songcount) + "  -----> DRIK!!")
    songcount += 1




