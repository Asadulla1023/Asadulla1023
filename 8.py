# file = open('8.txt', 'a')
# txt = int(input('Enter number: '))
# # file.write(txt + '\n')
# for i in range(1,11):
#     file.write(f'{txt} x{i} = {txt * i}\n')



# file.close()


# # w, a kiritsa bo'ladi



# rf = open('8.txt', 'r', encoding = 'utf-8')
# print(rf.read())
# rf.close()

# with open('8.txt', 'r') as rf:
#     rf.read()
#     print(rf.closed)
# print(rf.closed)

# with open('8.txt', 'r') as rf:
#     with open('8.txt', 'w') as wf:
#         wf.write(rf.read())

# with open('8.txt', 'r') as rf:
#     list = []
#     list.append(rf.read())

# with open('1.txt', 'w') as absd:
#     absd.write('Asadulla')
#     absd.seek(0)
#     absd.write('7')
#     # absd.write('Elbek')
#     print(absd.writable())


# with open('book.txt', 'r', encoding='utf-8') as book:
#     list = []
#     for line in book:
#         for word in line.strip().split(' '):
#             if not word == '':
#                 word = word.replace('.', '')
#                 word = word.replace(',', '')
#                 word = word.replace('_', '')
#                 word = word.replace('“', '')
#                 word = word.replace('”', '')
#                 word = word.replace(';', '')
#                 word = word.replace(':', '')
#                 word = word.replace('(', '')
#                 word = word.replace(')', '')
#                 word = word.replace('!', '')
#                 word = word.replace('?', '')
#                 print(word)

with