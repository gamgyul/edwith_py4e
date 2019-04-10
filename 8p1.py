inf = input('Enter input file: ')
all_line = list()
try:
    fhand = open(inf, 'r')
except:
    print('Error wrong file, program quited')
    quit()
for line in fhand:
    line = line.strip()
    list = line.split()
    all_line = all_line + list
    print(list)
all_line.sort()
print('all list:',all_line)