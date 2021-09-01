import pyautogui
import time


try:
    while True:
        x,y = pyautogui.position()
        position = f"x: {x} y: {y}"
        pixel_col = pyautogui.screenshot().getpixel((x,y))
        position += f"\tR: {pixel_col[0]}\tG: {pixel_col[1]}\tB: {pixel_col[2]}"
        print(position,end="")
        time.sleep(0.5)
        print("\b" * len(position),end="",flush=True)
except KeyboardInterrupt:
    print("Done")

