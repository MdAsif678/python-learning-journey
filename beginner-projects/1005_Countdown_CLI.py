import time
import subprocess

timer = int(input("Enter time in seconds: "))

while timer > 0:
    print(f"Time left: {timer}s")
    time.sleep(1)
    timer -= 1

print("\rBOOOOOOOOOOOOOOOOOOOOOOOOOOOM!!!!!!!!!!!!")
subprocess.run(["paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"])