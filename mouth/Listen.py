import speech_recognition as sp
from googletrans import Translator


def onlisten():
    r = sp.Recognizer()

    with sp.Microphone() as source:
        print("Lisning..")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recogizing..")
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    return query

def translation(Text):
    line = str(Text)
    tranlat = Translator()
    result = tranlat.translate(line)
    data = result.text
    print(f"You said: {data}")
    return data


def doning():
    Text = onlisten()
    data = translation(Text)
    return data
