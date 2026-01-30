colors = ['red', 'green', 'blue','red', 'black','red']
print(colors)
# print(colors.index('red',4))
ids =[104,3,67,89,23,45]
enumerate_colors = enumerate(colors)
zipped_colors = zip(ids, colors)
print(list(zipped_colors))
print(list(enumerate_colors))
for index, color in enumerate(colors,4):
    print(f"Index: {index}, Color: {color}")
for y in range(1,10,3):
    print(y)

numbers = [10,23,45,67,89,12,34,56]
res = [(num,"even") if num % 2 == 0 else (num,"odd") for num in numbers]
print(res)
print(list(filter(lambda x: x>10, numbers)))
print(list(map(lambda m:m/2, numbers)))
print(sum(numbers))
even = list(filter(lambda x: x%2==0, numbers))
print(even)