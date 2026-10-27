a = input("Zdanie: ")
b = len(a)

if b < 10:
    print("Pierwsze i ostatnie 5 liter: ZDANIE MUSI MIEĆ MIN.10 LITER!")

else:
    print("Pierwsze 5 Liter: %s" % a[:5])
    print("Ostatnie 5 liter: %s" % a[-5:])

print("Co druga litera: %s" % a[::2])
print("Na odwrót: %s" % a[::-1])
print("Bez pierwszej i ostatniej litery: %s" % a[1:-1])

srodek = a[(b - 1) // 2:b // 2 + 1]
print("Środkowa litera: %s" % srodek)

