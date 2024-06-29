sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for part in sounds:
    result += part.upper()
print(result)

instructors = []
instructors.extend(["Colt","Blue","Lisa"])
print(instructors)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
warm_colors = colors[:3]
print(warm_colors)
cold_colors = colors[2:]
print(cold_colors)

numbers = [1,2,3,4,5,6]
even = numbers[1::2]
odd = numbers[::2]
print(even, odd)

#swapping values
names = ["James", "Michelle"]
print(names)
names[0], names[1] = names[1], names[0]
print(names)

