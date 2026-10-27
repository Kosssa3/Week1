days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

numer = int(input("Enter a number from 1 to 7: "))

if numer >= 1 and numer <= 7:
    print("Day: %s" % days[numer - 1])
else:
    print("Error: numer must be from 1 to 7.")
