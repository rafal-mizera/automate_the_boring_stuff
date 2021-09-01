import re
names_list = [
'Satoshi Nakamoto',
'Alice Nakamoto',
'RoboCop Nakamoto',
'satoshi Nakamoto',
'Mr. Nakamoto',
'Nakamoto',
'Satoshi nakamoto']

names = "".join(names_list)

nakamotoRegex = re.compile(r"[A-Z][a-zA-Z]+ Nakamoto")

matches = []
for name in nakamotoRegex.findall(names):
    matches.append(name)
print(matches)

###################################################################
# How would you write a regex that matches a sentence where the first
# word is either Alice, Bob, or Carol; the second word is either eats, pets, or
# throws; the third word is apples, cats, or baseballs; and the sentence ends
# with a period? This regex should be case-insensitive. It must match the
# following:

sentences = ['Alice eats apples.',
'Bob pets cats.',
'Carol throws baseballs.',
'Alice throws Apples.',
'BOB EATS CATS.',
'RoboCop eats apples.',
'ALICE THROWS FOOTBALLS.',
'Carol eats 7 cats.']

sentences_to_regex = "".join(sentences)

sentencesRegex = re.compile(r"(Alice|Carol|Bob) (throws|eats|pets) (apples|cats|basketballs)",re.IGNORECASE)

matches = []
for sentence in sentencesRegex.findall(sentences_to_regex):
    matches.append(" ".join(sentence))

print(matches)