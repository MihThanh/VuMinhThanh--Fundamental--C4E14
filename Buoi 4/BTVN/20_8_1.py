counts = {}
data = "ThiS is String with Upper and lower case Letters"
for i in data.lower():
    counts[i] = counts.get(i, 0) + 1
counts_item = list(counts.items())
counts_item.sort()
for i in range(1, len(counts_item)):
    print(*counts_item[i])
