import re

def regexStripFunc(string,char = " "):
    myRegex1 = re.compile(f"^{char}+")
    myRegex2 = re.compile(f"{char}+$")
    a = myRegex1.sub("",string)
    result = myRegex2.sub("",a)
    return result


print(regexStripFunc("______Oto mój napis______","_"))








