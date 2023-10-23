import datetime
import speech
import pyttsx3
import speech_recognition
import wikipedia
import webbrowser

def speak(audio):
    engine = pyttsx3.init()
    #getter to retrieve values for voice
    voices = engine.getProperty('voices')

    #voices[1] sets female voice audio, set to 0 to change to male
    engine.setProperty('voice', voices[1].id)

    #To make the assistant speak
    engine.say(audio)

    #stops processing commands while processing queued
    engine.runAndWait()

def Take_query():
    Hello()

    while (True):
        query = takeCommand().lower()
        if "open buffalo state" in query:
            speak("Opening Buffalo State")
            webbrowser.open("https://suny.buffalostate.edu/")
            continue
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "what day is it" in query:
            Day()
            continue
        elif "what time is it" in query:
            Time()
            continue
        elif "bye" in query:
            speak("Goodbye. Stay tuned for my next updates")
            exit()

def takeCommand():
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print('Listening')

        r.pause_threshold = 0.9
        audio = r.listen(source)

        try:
            print("Attempting to recognize")

            Query = r.recognize_google(audio, language='en-in')
            print('command is: ', Query)
        except Exception as e:
            print(e)
            print("Please say that again")
            return "None"
        return  Query

def Time(self):
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    self.Speak(self, "The time is" + hour + "hours and" + min + "minutes")

def Hello():
    speak("Hello, I am your assistant. How can I help you?")
if __name__ == '__main__':
    Take_query()

def Day():
    day = datetime.datetime.today().weekday()+1
    Day_dict={1:'Monday', 2: 'Tuesday', 3: 'Wednesday',
              4: 'Thursday', 5:'Friday', 6:'Saturday',
              7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is "+day_of_the_week)

