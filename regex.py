import re



phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))

print(mo.group(0))

print(mo.group())
################################

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

################################
batRegex = re.compile(r'Bat(man|mobile|copter|bat|\d{3})')
mo = batRegex.search(' lost a wheel')
print(mo)

print(mo.group(1))

####################################
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

myRegex = re.compile(r"(CF)? Real Madryt")
mo5 = myRegex.search("CF Real Madryt pokonał FC Barcelonę 3:1")

print(mo5.group())

######################################
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
############################################
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowoman')
mo2.group()

############################################
robocop = re.compile(r'robocop',re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()

robocop.search('ROBOCOP protects the innocent.').group()

print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

############################################
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

phoneNumberRegex = re.compile(r"\d{3}-?\d{3}-?\d{3}")
print(phoneNumberRegex.sub("here is phone number", "My phone number is 793925972, my second phone number is 823-899-234"))

agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))