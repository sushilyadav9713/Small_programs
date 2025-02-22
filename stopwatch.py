import time

print('Press ENTER to begin. Afterward, press ENTER to know lap time. Press Ctrl-C to quit.')
input()
print("Started.")
startTime = time.time()
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'lap: {lapNum},total time:{totalTime},lap time:{lapTime}')
        lapNum +=1 
        lastTime = time.time()

except KeyboardInterrupt:
    print('Done.')