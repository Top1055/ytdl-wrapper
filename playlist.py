import youtube_dl

link = input("Link: ")
start = int(input("Start: "))
end = int(input("End: "))

ydl_opts = {
    'format': 'bestaudio/best',
    'playliststart':start,
    'playlistend':end,
    'ignoreerrors':True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl':'Songs/%(title)s.%(ext)s'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])