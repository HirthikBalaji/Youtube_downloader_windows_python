import pytube
link = str(input("enter the link to be downloaded ... : "))
yt = pytube.YouTube(link)
print(yt.title)
audio = str(input("enter audio or Video ... ? "))
if audio == "aud":
    print("downloading Audio ......")
    yt.streams.filter(only_audio=True).desc().first().download("./audio/")
elif audio == "vid":
    print("downloading Video ..... [takes some time]")
    yt.streams.filter(progressive=True).order_by("resolution").desc().first().download("./video/")