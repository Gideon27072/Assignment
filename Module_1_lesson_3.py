#finding the exponentiation of a number
print('finding the exponentiation of a number')

x = int(input('enter number: '))
y = int(input('enter number: '))

#check if the power is 0
if y==0:
    print('answer is 1')

else:
    x=x**y
    print(x)