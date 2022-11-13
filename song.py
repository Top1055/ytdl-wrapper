import youtube_dl

link = ""
songs = []
while link != "exit":
    link = input("Link: ")
    if link == "exit":
        break;
    else:
        songs.append(link)

ydl_opts = {
    'format': 'bestaudio/best',
    'ignoreerrors':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':'Songs/%(title)s.%(ext)s'
}

for song in songs:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])