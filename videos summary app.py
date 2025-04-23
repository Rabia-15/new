import os
import cv2
impoert streamlit as st
from pytube import YouTube
import subprocess
from langchain_groq import ChatGroq

#Directories
videos_directory = 'videos/'
frames_directory = 'frames/'
os.makedirs(videos_directory, exist_ok=True)
os.makedirs(frames_directory, exist_ok=True)

#Initialize Groq model
model = ChatGroq(
  model_name= "meta-llama/llama-4-scout-17b-16e-instruct"
)
#download YouTube videos using yt_dlp
def download_youtube_video(youtube_url):
    result = subprocess.run(
      [
        "yt-dp",
        "-f", "best[ext=mp4]",
        "-o",os.path.join(videos_directory, "%(title)s.%(ext)s"),
        youtube_url
      ],
      capture_output=True,
      text=True
    )
  if result.returncode != 0:
      raise runtimeError(f"yt-dlp-error:\n(result.stderr)")

download_files = sorted(
  os.listdir(videos_directory),
  key=lambda x: os.path.getctime(os.path.join(videos_directory, x)),
  reverse=True
  
