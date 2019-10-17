#!/usr/bin/env python
import os
from gtts import gTTS  # gTTS is a google text to speech utility

Text = "Hello ,World!"

print("please wait...processing")
TTS = gTTS(text=Text, lang='en-uk')

# Save to mp3 in current dir.
TTS.save("audio.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
os.system("start audio.mp3")
