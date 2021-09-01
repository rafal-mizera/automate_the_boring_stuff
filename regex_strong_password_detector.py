import re

def passwordStrengthDetector():
    regex_one = re.compile(r"[A-Z]+")
    regex_two = re.compile(r"[a-z]+")
    regex_three = re.compile(r"[0-9]+")
    regex_four = re.compile(r".{8,}")
    password = input("Podaj nowe hasło: ")
    if regex_one.search(password) != None and regex_two.search(password) != None and regex_three.search(password) != None and regex_four.search(password) != None:
        print("Twoje hasło zostało zmienione")
        new_password = password
        return new_password
    else:
        print("Nowe hasło nie spełnia wymagań bezpieczństwa")

passwordStrengthDetector()
