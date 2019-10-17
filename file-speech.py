#!/usr/bin/env python
import os
from gtts import gTTS

# You will need a text file named file.txt
# to play, put it in the current dir.
FLIST = open("file.txt", "r").read().replace("\n", " ")

print("please wait...processing file:")
TTS = gTTS(text=str(FLIST), lang='en-uk')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
print(FLIST)
os.system("start voice.mp3")
