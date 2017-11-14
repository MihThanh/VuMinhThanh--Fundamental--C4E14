# print("Word ", '\t\t', "Count")
# print('=' * 22)
# fo = open('alice.rtf','r').read()
# fo = fo.lower()
# print('a ', '\t\t', fo.count('a'))
# print('abide', '\t\t',fo.count('abide'))
# print('able', '\t\t',fo.count('able'))
# print('about', '\t\t', fo.count('about'))
# print('above', '\t\t', fo.count('above'))
# print('absence', '\t', fo.count('absence'))
# print('after', '\t\t', fo.count('after'))
# print('=' * 22)
# print('alice', '\t\t', fo.count('alice'))

# print("Word ", '\t\t', "Count")
# print('=' * 22)
# fo = open('alice.rtf','r').read()
# fo = fo.lower()


fo = open("alice.rtf")
text = fo.read() #Đọc toàn bộ file
fo.close()

ignore_words = ["\n", ",", ".", "?", "!", "\\", "\'", "(", ")", "{", "}"]
for i in ignore_words:
    text = text.replace(i, "")
words = text.split(" ")

words_count = {}
for word in words:
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word] += 1
print(words_count)
