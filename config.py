TOKEN = "5003009977:AAEKI0iGMSi_L4G4CdspDAlrQ-_Oi8rSgzs"

from gtts import gTTS
import os

def text_to_speech(mytext, lang):
    myobj = gTTS(text=mytext, lang=lang, slow=False)
    myobj.save("audio.mp3")