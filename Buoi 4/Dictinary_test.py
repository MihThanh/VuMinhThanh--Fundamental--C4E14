# p = ['Tuan Anh', 22, 3, 'Moc Chau', 2]
# print(p)

# person = {
#     'name' : 'Tuan Anh'
# }

person = {
    'name' : 'Tuan Anh',
    'age' : 22,
    'home' : 'Moc Chau',
    'exes' : 3
}

# print(person['home'])

# Thay đổi biến
person['home'] = 'Ha Noi'
print(person)

# Thêm key
person['project_count'] = 2
print(person)

# Xóa
del person['home']
print(person)
