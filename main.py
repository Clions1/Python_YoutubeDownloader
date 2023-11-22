import pytube
request = input("Select MP4 or MP3 : ")

path="C:/Users/Desktop/video and sounds"


if request == "MP4":
    url = input("enter MP4 url : ")
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
elif request == "MP3":
    url = input("enter MP3 url : ")
    pytube.YouTube(url).streams.get_audio_only().download(path)
else:
    print("Please enter a true value")