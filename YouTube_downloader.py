# creat by SmS.hZ
"""
download video, subtitle and other data from YouTube.com
"""

from pytube import YouTube

# ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
if link == 'test':
  link = 'https://www.youtube.com/watch?v=TX4Awy03dH0'
yt = YouTube(link)

# Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

ys = yt.streams.first()

# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
