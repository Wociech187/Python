import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1

engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",150)
while True:
    engine.say("Patryk nie ma jajek")
    engine.runAndWait()