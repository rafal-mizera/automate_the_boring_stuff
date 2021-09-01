import time

input("Press ENTER to start, press ENTER to 'click' the stopwatch, press ctrl+C to quit")
start = time.time()
print("Started...")
lastTime = start
lap_num = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - start,2)
        x = f"Lap # {lap_num}: {lapTime}s "
        y = f"Total: {totalTime}s"
        print(x.ljust(30) + y.ljust(20))
        lap_num += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("Done...")

