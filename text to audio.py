from gtts import gTTS
from playsound import playsound
import tempfile
import os

text = "hello,jaan log"

def do_tts(text):
    tts=gTTS(text)  #initialize object
    temp_file= tempfile.NamedTemporaryFile(suffix=".mp3" , delete = False)#tempfile will contail the audio/ if delete is set to true temp file will be deleted after audio isclosed
    tts.save(temp_file.name)
    file_url ="file://" + os.path.abspath(temp_file.name)
    return file_url



file_path =do_tts(text)
playsound(file_path)
os.remove(file_path)    