#dictionary containing key:value pair as num:squares

squares = {}
# for x in range(5,16):
#     squares[x] = x*x
    
#     print(squares)

#using dictionary comprehension
square = {x: x*x for x in range(5,16)}

print(square)