str = 'X-DSPAM-Confidence:0.8475'

colonn = str.find(':')
num = float(str[colonn+1:])

print("Number:", num)
str2 = 'Hello'
str2[2]='e'
print(str2)