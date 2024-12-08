from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=2lAe1cqCOXo&t=1s",use_oauth=True,allow_oauth_cache=True);
path = yt.streams.filter(progressive=True).get_highest_resolution().download()
print(path)