try:
    hours = int(input('Enter Hours'))
    rate = float(input('Enter Rate'))

    if hours >40 :
        pay = hours * rate * 1.5
    else :
        pay = hours * rate

    print('Pay:', pay)
except:
    print('Error, please enter numeric input')