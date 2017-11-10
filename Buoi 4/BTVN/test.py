counts = {}
data = "ThiS is String with Upper and lower case Letters"
for i in data.lower():
    counts[i] = counts.get(i, 0) + 1
item = list(counts.items())
item.sort()
for i in range(1, len(item)):
    print(*item[i])
