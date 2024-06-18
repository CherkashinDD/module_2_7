def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(5)
print_params(3, 6)
print_params(8, "новая строка", 9)
print_params(b=25)
print_params(c=[1, 2, 3])
print()
values_list = ["Амортизатор натяжителя", 1582, "рубля"]
values_dict = {'a': "Запчасть", 'b': "в наличии", 'c': 12}
print_params(*values_list)
print_params(**values_dict)
print()
values_list_2 = ["Но!", "Это не точно :)"]
print(*values_list_2, 42)
