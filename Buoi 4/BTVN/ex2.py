prices = {
  'banana' : 4,
  'apple' : 2,
  'orange' : 1.5,
  'pear' : 3
}
stock = {}
stock['banana'] = 6
stock['apple'] = 0
stock['orange'] = 32
stock['pear'] = 15

list1 = list(prices.keys())
list2 = list(prices.values())
list3 = list(stock.values())
for i in range(len(list1)):
    for j in range(i,len(list3)):
        print(list1[i],':', list3[j])
        for k in range(j ,len(list2)):
            print("prices:", list2[k])
            print()
            break
        break

totals = []
for q in range(len(list2)):
    for p in range(q, len(list3)):
        total = list2[q] * list3[p]
        totals.append(total)
        for k in range(p, len(list1)):
            print("Prices {0}: {1}".format(list1[k],total))
            break
        break
total_prices = 0
total_prices = sum(totals)
print("Total prices: ", total_prices)
