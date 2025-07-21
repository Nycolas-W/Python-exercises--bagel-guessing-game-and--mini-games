# Concession stand program
menu = {"pizza": 3.00,
        "nachos": 4.56,
        "popcorn": 6.00,
        "fries": 2.56,
        "chips": 1.00,
        "pretzel": 3.00,
        "soda": 3.00,
        "lemohade": 4.25}

cart = []
total = 0

print('--------MENU-------')
for key, value in menu.items():
    print(f'{key:9}: ${value:.2f}')#:9 e .2f sao apenas espaços depois de key a value
print('-------------------')

while True:
    food = input('What food to add in your cart? PRESS Q TO QUIT ').lower()
    if food == 'q':
        break
    elif menu.get(food): #lembrando get method recebe o valor entre parensesis
        cart.append(food)
    else:
        print('Food not available on our menu, try again')

for food in cart:
    total += menu.get(food)#como apenas o valor é em int/float so ele é somado no pirint
    print(food, end=' ')
cart_values = [menu[item]for item in cart] #maneira diferente de mostrar os valores do discionario 

print(f'your cart {cart}')
print(f'Total ${total:.2f} and {cart_values}')