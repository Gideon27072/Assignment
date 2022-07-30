#function to return variable
def maximum(a,b,c):
    return max(a,b,c)

a = int(input('enter number: '))
b = int(input('enter number: '))
c = int(input('enter number: '))

max_num = maximum(a,b,c)

print('maximum number is' +   str (max_num))