import pyttsx3
import datetime
import wikipedia
import pyaudio
import webbrowser
import speech_recognition as sf
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning! , sir ')
    elif hour>=12 and hour<18:
        speak('Good Afternoon , sir')
    else:
        speak('Good Evening/Night , sir ')
    speak('I am jarvis , sir how may i help you ?')
#takes microphone input afrom the user and returns string output
def takeCommand():
    r=sf.Recognizer()

    with sf.Microphone() as source:
        print('Listening ...')
        r.adjust_for_ambient_noise(source, duration=1)
        #r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-us')
        print(f"---------> : {query}\n")
    except Exception as e:
        #print(e)
        print('------ kindly Say that again ----- ')
        # return 'None'
    return query
query=takeCommand().lower()
# wishMe()
# print(query)
import nltk
# nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sid.polarity_scores(query)['Positive'] = sid.polarity_scores(query).pop('pos')
sid.polarity_scores(query)['Negative'] = sid.polarity_scores(query).pop('neg')
sid.polarity_scores(query)['Neutral'] = sid.polarity_scores(query).pop('neu')
print(sorted(sid.polarity_scores(query).items(),key=lambda x:x[1],reverse=True)[0])
# while True:
#     if 'wikipedia' in query:
#         speak('Searching wikipedia...')
#         query=query.replace('wikipedia','')
#         results=wikipedia.summary(query,sentences=2)
#         speak('according to wikipedia')
#         speak(results)
#     elif 'open youtube' in query:
#         webbrowser.open('youtube.com')
#         break
#     elif 'the time' in query:
#         strTime = datetime.datetime.now().strftime("%H:%M:%S")
#         speak(f"Sir, the time is {strTime}")
#         break
#     elif 'temperature' in query:
#         webbrowser.open('https://timesofindia.indiatimes.com/weather/city-Chandigarh.cms')
#         break
#     else:
#         webbrowser.open('google.com')
#         break