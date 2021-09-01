import os


def mad_libs(file, new_file):
    new_text = ""
    with open(file, "r") as f:
        data = f.read().split(" ")
        for word in data:
            if word == "ADJECTIVE":
                new_word = input("Enter an adjective: ")
                new_text += new_word + " "
            elif word == "NOUN":
                new_word = input("Enter an noun: ")
                new_text += new_word + " "
            elif word == "VERB":
                new_word = input("Enter an verb: ")
                new_text += new_word + " "
            else:
                new_text += word + " "
    with open(new_file, "w") as nf:
        nf.write(new_text)
    print(new_text)


mad_libs(r"C:\temp\nowy_tekst.txt", r"C:\temp\jeszcze_nowszy_tekst.txt")
