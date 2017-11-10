teen_dict = {
    'ns' : 'Nghĩa là nói. Hành động giao tiếp của con người',
    'ngta' : 'Nghĩa là người ta. Ý nói người khác không liên quan đến mình',
    'cng' : 'Nghĩa là con người. Tên gọi chung của loài người',
    'gato' : 'Nghĩa: Ý nói sự ghen tị, khó chịu với người nào đó vì hơn mình',
    'lm' : 'Nghĩa là: Lắm',
}

while True:
    print(*teen_dict)
    n = input("Nhập từ bạn  muốn tra cứu: ")
    if n in teen_dict:
        print(teen_dict[n])
    else:
        print("Không tìm thấy từ cần tra")
        m = input("Bạn muốn thêm từ không: ").lower()
        if m == 'y':
            key = input("Nhập từ bạn muốn thêm: ")
            mean = input("Nghĩa: ")
            teen_dict[key] = mean
            print("Đã thêm thành công")
            n = input("Nhập từ bạn  muốn tra cứu: ")
            if n in teen_dict:
                print(teen_dict[n])
        elif m == 'n':
            break
