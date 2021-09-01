import re, os


def regex_search(dir):
    ex = input("Wprowadź szukaną frazę: ")
    regex = re.compile(str(ex))
    for file in os.listdir(dir):
        if file.endswith("txt"):
            path = os.path.join(dir, file)
            with open(path, "r") as f:
                for line in f:
                    if regex.search(line):
                        print(line)



regex_search(r"C:\temp")
