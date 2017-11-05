menu = ['com', 'pho', 'chao']
# print(menu)
# # menu.remove('chao')
# # print(menu)
# if 'com' in menu:
#     menu.remove('com')
#     print(menu)
# else:
#     print("Khong tim thay")

print(*menu, sep = ', ')
print('*' * 10)
n = input("Nhap vao mon ban muon xoa: ")
if n in menu:
    menu.remove(n)
    print(*menu,sep = ', ')
else:
    print("Mon ban can xoa khong co trong menu")
