import pyautogui
import time

namefield = (443,404)
submit = (401,551)
submitButtonColor = (119,119,119)
submitAnotherLink = (495, 261)


formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
'robocop': 4, 'comments': 'Tell Bob I said hi.'},
{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,'comments': 'n/a'},{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
'robocop': 1, 'comments': 'Please take the puppets out of thebreak room.'}, {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust.'}]


for person in formData:
    time.sleep(3)
    pyautogui.scroll(-2000,0.5)
    while not pyautogui.pixelMatchesColor(submit[0],submit[1],submitButtonColor):
        time.sleep(0.5)
    print(f"Entering {person} data...")
    pyautogui.scroll(4000,1)
    time.sleep(2)
    pyautogui.click(namefield)
    time.sleep(2)
    pyautogui.typewrite(person["name"] + "\t")
    time.sleep(2)
    pyautogui.typewrite(person["fear"] + "\t")


    if person["source"] == "wand":
        pyautogui.typewrite("down")
        pyautogui.typewrite(["enter","\t"])
    elif person["source"] == "amulet":
        pyautogui.typewrite(["down","down"])
        pyautogui.typewrite(["enter","\t"])
    elif person["source"] == "crystal ball":
        pyautogui.typewrite(["down","down","down"])
        pyautogui.typewrite(["enter","\t"])
    else:
        pyautogui.typewrite(["down","down","down","down"])
        pyautogui.typewrite(["enter","\t"])

    time.sleep(1)

    if person["robocop"] == 1:
        pyautogui.typewrite([" ","\t","\t"])
    elif person["robocop"] == 2:
        pyautogui.typewrite(["right","\t","\t"])
    elif person["robocop"] == 3:
        pyautogui.typewrite(["right","right","\t","\t"])
    elif person["robocop"] == 4:
        pyautogui.typewrite(["right","right","right","\t","\t"])
    else:
        pyautogui.typewrite(["m","\t","\t"])

    time.sleep(2)


    pyautogui.typewrite(person["comments"] + "\t")

    pyautogui.press("enter")
    print("Form was submitted succesfully...")
    time.sleep(5)
    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])










