import pyttsx3 as tts
import speech_recognition as sr
import Commands
import weather
import randfacts
import jokes
import datetime


def main():
    say("Hey There, What shall I do")
    task = listen()
    if "information" in task:
        say("What do you need information on")
        topic = listen()
        action = Commands.Commands()
        action.getInfo(topic)
    elif "play" and ("video" or "song") in task:
        if "song" in task:
            say("What song would you like?")
        else:
            say("What video would you like?")
        vid = listen()
        say(f"Sure thing, Playing {vid}")
        action = Commands.Commands()
        action.getVid(vid)
    elif "weather" in task:
        say("For which city")
        city = listen()
        action = weather.Weather()
        say(action.getWeather(city=city))
    elif "random" and "fact" in task:
        say("Did you know " + randfacts.get_fact(False))
    elif "joke" in task:
        joke = jokes.jokes.get_joke()
        print(joke["setup"])
        say(joke["setup"])
        print(joke["punchline"])
        say(joke["punchline"])
    elif "date" or "time" in task:
        dt = datetime.datetime.today().strftime("%I %M %p %A %B %Y")
        data = dt.split(" ")
        print(f"It's {data[0]}:{data[1]}{data[2]} on {data[3]}, {data[4]} {data[5]}")
        say(f"It's {data[0]}:{data[1]}{data[2]} on {data[3]}, {data[4]} {data[5]}")


# Listens to the microphone and returns what was said
def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.energy_threshold = 10000
        listener.adjust_for_ambient_noise(source, 0.5)
        print("Listening...")
        audio = listener.listen(source)
    try:
        text = listener.recognize_google(audio)
    except sr.RequestError:
        print("Unable to connect to Api")
    except sr.UnknownValueError as e:
        say("Sorry I did not catch that")
        listen()
    else:
        return text


# converts the text to speech and speaks it
def say(text):
    engine = tts.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 130)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    main()
