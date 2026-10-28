days = ("Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday")

temperatures = (18, 21, 19, 24, 22, 17, 20)

total = 0

for i in range(len(days)):
    print("%s: %d°C" % (days[i], temperatures[i]))
    total += temperatures[i]

average = total / len(temperatures)

highest = temperatures[0]
lowest = temperatures[0]
highest_day = days[0]
lowest_day = days[0]

for i in range(len(temperatures)):
    if temperatures[i] > highest:
        highest = temperatures[i]
        highest_day = days[i]

    if temperatures[i] < lowest:
        lowest = temperatures[i]
        lowest_day = days[i]

days_above_average = 0

for i in range(len(temperatures)):
    if temperatures[i] > average:
        days_above_average += 1

fahrenheit_temperatures = []

for i in range(len(temperatures)):
    fahrenheit = temperatures[i] * 9 / 5 + 32
    fahrenheit_temperatures.append(fahrenheit)

print("Average temperature: %.2f°C" % average)
print("Highest: %d°C on %s" % (highest, highest_day))
print("Lowest: %d°C on %s" % (lowest, lowest_day))
print("Days above average: %d" % days_above_average)

print("\nTemperatures in Fahrenheit:")
for i in range(len(days)):
    print("%s: %.1f°F" % (days[i], fahrenheit_temperatures[i]))
