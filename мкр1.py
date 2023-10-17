matrix = [
    [123, 25, 1],
    [67, -21, 311],
    [45, 1.2, 6]
]

print("Початковий масив:")
for row in matrix:
    print(row)

averages = []
for row in matrix:
    average_value = sum(row) / len(row)
    averages.append(average_value)

for i in range(len(averages)):
    for j in range(i + 1, len(averages)):
        if averages[i] > averages[j]:
            averages[i], averages[j] = averages[j], averages[i]
            matrix[i], matrix[j] = matrix[j], matrix[i]

print("Середні значення рядків:")
for avg in averages:
    print(avg)

print("Відсортований масив:")
for row in matrix:
    print(row)