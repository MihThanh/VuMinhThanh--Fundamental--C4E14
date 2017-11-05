menu = ['T-Shirt', 'Sweater']
while True:
    n = input("Welcome to our shop, what do you want (C, R, U, D): ")
    if n == "c":
        new_item = input("Enter new item: ")
        menu.append(new_item)
        print(*menu, sep = ', ')

    elif n == "r":
        print(*menu, sep = ', ')

    elif n == "u":
        poision = int(input("Update position: "))
        index = poision - 1
        new_name = input("New name: ")
        menu[index] = new_name
        print(*menu, sep = ', ')

    elif n == "d":
        poision1 = int(input("Delete poision: "))
        index1 = poision1 + 2
        for index1, item in enumerate(menu):
            menu.remove(item)
            break
        print(*menu, sep = ', ')
    elif n == 'thoat':
        break
