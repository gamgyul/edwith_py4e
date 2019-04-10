inf= input ('Enter input file')
try:
    fhandle = open(inf, 'r')
except:
    fhandle = open('clown.txt','r')

word_dict= dict()
for line in fhandle:
    word_list = line.split()
    for word in word_list:
        word_dict[word]= word_dict.get(word, 0) + 1

print(word_dict)
count_list = list()
for (k,v) in word_dict.items():
    count_list.append((v,k))
    count_list.sort(reverse=True)
print('count_list',count_list)