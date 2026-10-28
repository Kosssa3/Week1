grades = [45, 72, 88, 51, 90, 63]

total = 0
passing = 0
range_0_49 = 0
range_50_69 = 0
range_70_89 = 0
range_90_100 = 0

for i in range(len(grades)):
    grade = grades[i]

    # Initialize highest and lowest using the first grade
    if i == 0:
        highest = grade
        lowest = grade

    total += grade

    if grade >= 50:
        passing += 1

    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

    if grade <= 49:
        range_0_49 += 1
    elif grade <= 69:
        range_50_69 += 1
    elif grade <= 89:
        range_70_89 += 1
    else:
        range_90_100 += 1

average = total / len(grades)

print("Total: %d" % total)
print("Average grade: %.2f" % average)
print("Passing grades: %d" % passing)
print("Highest grade: %d" % highest)
print("Lowest grade: %d" % lowest)

print("Grades from 0-49: %d" % range_0_49)
print("Grades from 50-69: %d" % range_50_69)
print("Grades from 70-89: %d" % range_70_89)
print("Grades from 90-100: %d" % range_90_100)
