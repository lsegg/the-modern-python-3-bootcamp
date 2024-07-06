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

# list comprehension
print([x*10 for x in numbers])
print([num*10 for num in range(1,7)])

# LC with conditional logic
numbers = range(1,101);
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
print(evens, '\n', odds)

print([num*2 if num % 2 == 0 else num/2 for num in numbers])

with_vowels = "This is so much fun!"
without_vowels = ''.join(char for char in with_vowels if char not in 'aeiou')
print(without_vowels)

nums1 = [1,2,3,4]
nums2 = [3,4,5,6]
nums_intersection = [num for num in nums1 and nums2 if num in nums1 and num in nums2]
print(nums_intersection)

# multidimensional/nested lists
nested_list = [[1,2,3], [4,5,6], [7,8,9]]
[[print(val) for val in l] for l in nested_list]

board = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for _ in range(1,4)]
print(board)