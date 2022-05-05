names = []
balls = []

for index in range(7):
    names.append(input("Ф.И.О: "))
    balls.append(float(input("Баллы: ")))

minimal = min(balls)
maximum = max(balls)
minimal_index = balls.index(minimal)
maximum_index = balls.index(maximum)


print("Максимальный балл имеет " + names[maximum_index] + ", значение для данного студента равно " + str(maximum))
print("Минимальный балл имеет " + names[minimal_index] + ", значение для данного студента равно " + str(minimal))
