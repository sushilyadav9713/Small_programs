import threading, time
print('start')
def takeANap():
    time.sleep(5)
    print('wake up')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('end')