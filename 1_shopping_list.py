lista_zakupow = []

while True:
    produkt = input("Enter a product (or 'done'): ").strip()

    if produkt == "done":
        break
    elif produkt == "":
        continue
    elif produkt in lista_zakupow:
        print("%s is already on the list." % produkt)
    else:
        lista_zakupow.append(produkt)

if lista_zakupow:
    remove_product = input("Which product should be removed? ").strip()

    if remove_product in lista_zakupow:
        lista_zakupow.remove(remove_product)
        print("%s was removed." % remove_product)
    elif remove_product == "":
        print("No product entered; nothing was removed.")
    else:
        print("%s is not on the list." % remove_product)
else:
    print("The shopping list is empty.")

lista_zakupow.sort()

print("\nlista_zakupow:")
for i in range(len(lista_zakupow)):
    print("%d. %s" % (i + 1, lista_zakupow[i]))

print("Liczba Produktów: %d" % len(lista_zakupow))
