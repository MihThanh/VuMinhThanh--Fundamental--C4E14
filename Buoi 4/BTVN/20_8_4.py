fo = open('alice.rtf', 'r').read()
alice = fo.lower()
long_word = ""
count = 0
change = ",.[]();''\\\"?!-"
for i in change:
    alice = alice.replace(i, ' ')
for i in alice.split():
    if len(i) > len(long_word):
        long_word = i
for i in long_word:
    count += 1
print("Longgest word:",long_word)
print("Long:",count)
