import sys
import time
from io import BytesIO
from datetime import datetime
from gtts import gTTS
from mpg123 import Mpg123, Out123


def main():
    while True:
        try:
            now = datetime.now()
            if now.time().second % 10 == 0:
                time_str = now.strftime("%H:%M:%S")
                audio = gTTS(text=time_str, lang="en", slow=False)

                fp = BytesIO()
                audio.write_to_fp(fp)
                fp.seek(0)

                mp3 = Mpg123()
                mp3.feed(fp.read())

                out = Out123()

                for frame in mp3.iter_frames(out.start):
                    out.play(frame)
            time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)

    # while True:
    #     try:
    #         now = datetime.now()
    #         seconds = now.time().second
    #         if seconds % 10 == 0:
    #             time_str = now.strftime("%H:%M:%S")
    #             engine.say(time_str)
    #             engine.runAndWait()
    #         time.sleep(1)
    #     except:
    #         engine.say("Goodbye!")
    #         engine.runAndWait()
    #         sys.exit(1)


if __name__ == "__main__":
    main()
