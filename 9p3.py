inf = input('Enter input file: ')
all_line = list()
tmp = dict()
try:
    fhand = open(inf, 'r')
except:
    fhand = open('mbox-short.txt', 'r')
    #print('Error wrong file, program quited')
    #quit()
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        print(line)
        line_list = line.split()
        if len(line_list) >=3:
            day_week = line_list[2]
            tmp[day_week] = tmp.get(day_week, 0) +1
print(tmp)
    #list = line.split()
    #all_line = all_line + list
    #print(list)
#all_line.sort()
#print('all list:',all_line)