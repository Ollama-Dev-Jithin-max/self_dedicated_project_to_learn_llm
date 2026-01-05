import speech_recognition as sr 
recognizer = sr.Recognizer()
from vosk import KaldiRecognizer,Model
import json
model=Model("vosk-model-en-us-0.22")
rec = KaldiRecognizer(model, 16000)
def listen():
#  f_text=recognizer.recognize_vosk(mic)
  with sr.Microphone() as source:
   recognizer.dynamic_energy_threshold = False
#recognizer.energy_threshold = 500  # Low sensitivity (quiet room)
   recognizer.energy_threshold = 4000 # High sensitivity (loud room)
   recognizer.adjust_for_ambient_noise(source, duration=2)
   mic = recognizer.listen(source)
   raw_data = mic.get_raw_data(convert_rate=16000, convert_width=2)
   rec.AcceptWaveform(raw_data)
   result = json.loads(rec.Result())
  return result['text']
from AppOpener import open