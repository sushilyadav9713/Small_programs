import time

def calcProd():
    product = 1
    for i in range(1,1000):
        product = i * product
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('the result is %s digits long' % len(str(prod)) )
print('Time taken to run the program %s' %(endTime-startTime))