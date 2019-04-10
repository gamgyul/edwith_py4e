string='Connect Foundation!'
print(len(string))

inf = input('Enter input file: ')
try:
    fhand = open(inf, 'r')
except:
    print('Error wrong file, program quited')
    quit()

count =0
#inp = fhand.read()
#print(len(inp))
for line in fhand:
    line =line.upper()
    line = line.strip()
    print(line)
