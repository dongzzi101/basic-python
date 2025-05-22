# List
# tuple : 값 못바꿈
# dictionary : 키, 값 쌍으로


my_list = [1, 2, 3]
print(my_list)
print(type(my_list))

students = ['nana', 'kayler', 'helerty']
print(students)

for student in students:
    print(student)

students.append('meta')

for student in students:
    print(student)

students[0] = 'facebook'
for std in students:
    print(std)

my_tuple = ('a', 'b', 'c')
print(my_tuple)

# my_tuple[0] = 'C'

my_dict = {'kaka': '남', 'ray': '여'}
print(my_dict['kaka'])

my_dict['kaka'] = '여'
print(my_dict['kaka'])


# 타입 변경
my_int = 1
print(type(my_int))
print(my_int)
my_int = float(my_int)
print(my_int)

my_int = str(my_int)
print(type(my_int))
