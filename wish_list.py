products = []

for a in range(1, 4):
    product = input("Jaki produkt: " + str(a) + ": ")
    products.append(product)

print()
print("Your list:", products)

remove_product = input("Co chcesz usunąć? ")

if remove_product in products:
    products.remove(remove_product)
    print(remove_product, "has been removed.")
else:
    print(remove_product, "was not found.")

print("Final list:", products)
