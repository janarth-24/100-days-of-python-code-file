import time

start=int(input("Enter the number to start the countdown :" ))

print("==========CountDown Begins========")
while start:
    print(start)
    time.sleep(1)
    start-=1
print("========CountDown Completed========")
