
import time

timer = input("Enter the time you want to set your alarm at(HH:MM:SS): ")

while True:
    current = time.strftime("%H:%M:%S")
    if current == timer:
        print("Times up, ITS TIME TO WAKEUP!!!!")
        break
    time.sleep(1)
    print(time.strftime("%H:%M:%S"))
