import sys
import pyttsx3
import time
from datetime import datetime


def main():
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    while True:
        try:
            now = datetime.now()
            seconds = now.time().second
            if seconds % 10 == 0:
                time_str = now.strftime("%H:%M:%S")
                engine.say(time_str)
                engine.runAndWait()
            time.sleep(1)
        except:
            engine.say("Goodbye!")
            engine.runAndWait()
            sys.exit(1)


if __name__ == "__main__":
    main()
