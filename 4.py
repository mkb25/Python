my_set = {1,2,3,4,5,6,7,8,9,10}
myset = {1,2,3,4,5,6,7,8,9,89}
my_set2 = {"a","b","c","d","e","f","g"}
print(my_set)
print(type(my_set))
print(my_set2 | my_set)
print(my_set.union(my_set2))
print(my_set-myset)
print(my_set^myset)
print(myset.isdisjoint(my_set2))
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product in products.items():
    print(product)
