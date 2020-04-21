my_pizzas = ['cheese', 'pepperoni', 'olive']
friend_pizzas = my_pizzas[:]

#Add new pizzas
my_pizzas.append('veggie')
friend_pizzas.append('combo')

#Use for loop
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)
