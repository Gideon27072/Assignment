#creating a list of integers between 5.5 and 20.5
i = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_no = list(filter(lambda x: (x % 2 == 0), i))

print("all even numbers in the list: ", even_no)

odd_no = list(filter(lambda x: (x % 2 != 0), i))

print("all odd numbers in the list: ", odd_no)

even_count = len(list(filter(lambda x: (x % 2 == 0), i)))

print("all even numbers that are in the list: ", even_count)

square = list(map(lambda x: (x**2), i))

print(square)

cube = list(map(lambda x: (x**3), i))
print(cube)