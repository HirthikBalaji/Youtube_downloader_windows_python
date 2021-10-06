import pytube
import urllib.request
import re
q = str(input("enter the link to be downloaded ... : "))
html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={q}")
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
link = "www.youtube.com/watch?v=" + video_ids[0]
print(pytube.YouTube(link).title)
yt = pytube.YouTube(link)
audio = str(input("enter audio or Video ... ? "))
if audio == "aud":
    print("downloading Audio ......")
    yt.streams.filter(only_audio=True).desc().first().download("./audio/")
elif audio == "vid":
    print("downloading Video ..... [takes some time]")
    yt.streams.filter(progressive=True).order_by("resolution").desc().first().download("./video/")
