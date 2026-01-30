pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
    "name": "My Favorite Pizza",
    "calories": 2500,
    "price": 12.99
}
a =[ 1,2,3,4,5]
pizza1 = pizza.items()
print(a[1])
print("IOP")
print(f"You ordered a {pizza['crust']} crust pizza ")
print(pizza1)
print(list(enumerate(pizza1)))
print(type(enumerate(pizza1)))
print(type(pizza1))
print(type(pizza))
print('\n',pizza,'\n')
pizza.update({'price':10.00})
print('\n',pizza,'\n')