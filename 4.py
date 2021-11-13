# name = ['Xasan', 'Asadulla', 'Xusan', 'Elbek', 'Xasan']
# name[3] = 'Qobiljon'
# name.insert(2,'Isroil')
# name.remove('Xasan')
# name.remove('Xasan')
# name.insert(0,'Elbek')
# name.remove('Elbek')
# del name[2:5]
# print(name)
# from random import randint
# a = int(input('son kiriting: '))
# list = []
# i = 0
# while i < a:
#     list.append(randint(0, 100))
#     i+=1

# print(list)
from random import randint
print([randint(0, 100)for i in range(int(input('Enter number: ')))])