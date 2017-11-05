# menu = ['com ', 'bun', 'pho']
# print(menu)
# menu.append("cha xien")
# print(menu)
# # in vao bat ky cho nao
# menu.insert(0, 'com nieu')
# print(menu)

#Tao menu goi mon an
menu = ['com', 'chao', 'pho']
print(*menu, sep = ', ')
print("* "* 10)
while True:
    n = input("Ban muon them mon gi: ")
    if n == 'thoat':
        break
    else:
        menu.append(n)
        print(*menu, sep = ', ')
        
