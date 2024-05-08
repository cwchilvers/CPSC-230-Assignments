my_list = [1.6, 2.7, 3.8, 4.9]
new_list = []
a_list =[]

for val in my_list:
    temp = str(val)
    a_list.append(temp.split('.'))


for val in a_list:
    new_list.append(int(val[0]))

my_str = ':'.join(val)

print(my_list)
print(a_list)
print(new_list)
print(val)
print(my_str)
