while True:
    n = input("Nhap user: ");
    if n.upper() != "C4E": #lower(): bien thanh chu thuong
        print("User khong dung")
    else:
        a = input("Nhap password: ")
        if a != "minhthanh":
            print("password sai")
        else:
            print("Xin chao Minh Thanh")
