distinc_powers = []
for i in range(2,101):
    for j in range(2,101):
        power = i**j
        if power not in distinc_powers:
            distinc_powers.append(power)
print(len(distinc_powers))