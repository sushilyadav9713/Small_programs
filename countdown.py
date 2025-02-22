import time, subprocess

timeleft = 10 
while timeleft > 0:
    print(timeleft)
    time.sleep(1)
    timeleft = timeleft -1

subprocess.Popen(['start','alarm.wav'],shell=True)