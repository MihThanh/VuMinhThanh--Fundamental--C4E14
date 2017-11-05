menu = ['com ', 'bun', 'pho']
for index, item in enumerate(menu):
    print(index + 1, ', ', item, sep = '')

n = int(input("Vi tri muon cap nhat: "))
index= n - 1

new_ten = input("Ten muon cap nhat: ")
menu[index]= new_ten

for index, item in enumerate(menu):
    print(index + 1, ', ', item, sep = '')
