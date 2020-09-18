import soundcloud

# create a client object with access token
client = soundcloud.Client(access_token='YOUR_ACCESS_TOKEN')

# get playlist
playlist = client.get('/playlists/1129112860')

# list tracks in playlist
for track in playlist.tracks:
    print(track['title'])
