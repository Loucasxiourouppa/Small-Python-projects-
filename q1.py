import math

eaters = input("How many people are attending the party?")

pieces = input("How many pieces will everyone eat on average?")

pizzas = float(eaters) * float(pieces)
orders_needed = math.ceil(pizzas/8)
print(orders_needed)
