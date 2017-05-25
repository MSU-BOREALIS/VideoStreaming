import time
from os import system
from subprocess import call




def ten_second_record_subprocess():
    call(["ffmpeg", "-i rtsp://@127.0.0.1:8554/", "-vcodec copy", "-acodec none", "-f mp4 testing.mp4"])
    time.sleep(10)
    call(["killall ffmpeg"])


def ten_second_record_os():
    timestr = time.strftime("%d%m%Y-%H%M%S")
    print timestr
    system("/opt/stream/bin/ffmpeg -i rtsp://127.0.0.1:8554/ -vcodec copy -acodec none -f mp4 " + timestr + ".mp4 &")
    time.sleep(10)
    system("killall ffmpeg")
    


def main():
    for i in range (0,10):
        ten_second_record_os()

if __name__ == "__main__":
    main()
