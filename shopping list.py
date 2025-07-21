#shopping list

products = []
prices = []
total = 0

while True :
    product= str(input('what products you wanna buy ? if none type ( Q ) to close it ').lower())
    if product == "q":
        print('list closed! ')
        break
    elif product != "q":
        price = float(input(f'whats the price of the {product}? '))
        products.append(product)
        prices.append(price)
    else:print('invalid')
    
print('-----YOUR SHOPPING CART-----')
for i,product in enumerate(products):
    #i variable is for every item on each list hence all have [i]
    print(f"{products[i]} - { prices[i]:.2f}")
    total += prices[i] 

print(f'Total = ${total}')