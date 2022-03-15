import time

start = time.time()
current = 0
while start-current != 60:
    print("Hello World")
    current += time.time()
#
# print(time.ctime())