import pyperclip, re

phoneRegex = re.compile(r'''(
(\d{2}|\(\d{2}\))? # area code
(\s|-|\.)? # separator
(\d{2}) # first 2 digits
(\s|-|\.)? # separator
(\d{2}) # 2 digits
(\s|-|\.)? # extension
(\d{3}) #last two digits
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for group in phoneRegex.findall(text):
    phone_num = "-".join([group[1],group[3],group[5],group[7]])
    matches.append(phone_num)

for group in emailRegex.findall(text):
    matches.append(group[0])

if len(matches) > 0:
    result = "\n".join(matches)
    pyperclip.copy(result)
    print(result)
else:
    print("Nie znaleziono numerów telefonu ani adresów email")

with open(r"C:\temp\lista_numerow_i_emaili.txt","w") as f:
    f.write(result)