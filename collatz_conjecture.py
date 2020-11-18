num = int(input("Type x_0:   "))

trials = 0
while num != 1 and num >= 0:
    if num % 2 == 0:
        num = num / 2
        trials += 1
    else:
        num = 3 * num + 1
        trials += 1

print("Number of trials: ", trials)