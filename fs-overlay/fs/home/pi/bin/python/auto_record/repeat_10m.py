import time
from os import system
from subprocess import call



def ten_second_record_subprocess():
    call(["ffmpeg", "-i rtsp://@127.0.0.1:8554/", "-vcodec copy", "-acodec none", "-f mp4 testing.mp4"])
    time.sleep(10)
    call(["killall ffmpeg"])

#this function will record video for 10 minutes
#ffmpeg takes about 2 seconds to start up and start recording
#hence 602 seconds
def ten_minute_record_os():
    timestr = time.strftime("%d%m%Y-%H%M%S")
    print timestr
    system("/opt/stream/bin/ffmpeg -i rtsp://127.0.0.1:8554/ -vcodec copy -acodec none -f mp4 " + timestr + ".mp4 &")
    #ffmpeg takes about 2 seconds to start recording
    #so for a 10 min chuck 2 more seconds are added.
    time.sleep(602)
    system("killall ffmpeg")
    


def main():
    time.sleep(150)
    #will wait for the pi to boot up if this is in the root crontab
    #with a @reboot configuration
    while (True):
        ten_minute_record_os()

#make sure that the real time clock is powered and set to the correct 
#date before running on a flight. Otherwise the time and date will be incorrect on the payload.

if __name__ == "__main__":
    main()
