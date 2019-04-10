sum = 0
count = 0
while True:
    try:
        num = input('Enter a number')
        num = float(num)
    except:
        if num == 'done':
            break
        else:
            print('Invalid input')
            continue
    sum = sum + num
    count = count +1
print('sum:',sum)
print('cnt:',count)
print('avg:',sum/count)
