from pytube import YouTube
from progress.bar import Bar
import os
import sys


if len(sys.argv) != 2:
    sys.exit('Invalid use')

yt = YouTube(sys.argv[1])
audio = yt.streams.filter(only_audio=True).first()

destination = '/users/quaku/Downloads'

out_file = audio.download(output_path=destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)