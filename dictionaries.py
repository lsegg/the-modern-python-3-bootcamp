# Two ways of making a dictionary
cat = {
  "name": "Blue",
  "age": 3,
  "is_cute": True
}
cat2 = dict(name="Kitty", age=0.5, is_cute=True)
print(cat, cat2)

artist = {
  "first": "Neil",
  "last": "Young",
}
full_name = artist["first"] + " " + artist["last"]
print(full_name)

instructor = {
  "name": "Colt",
  "owns_dog": True,
  "favourite_language": "Python"
}

for k,v in instructor.items():
  print(f"key is {k} and value is {v}")


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = 0
for v in donations.values():
  total_donations += v
print(total_donations)

person = {"ocupation": "instructor"}
person.update(instructor)
print(person)

playlist = {
  "title": "patagonia bus",
  "author": "colt steele",
  "songs": [
    {
      "title": "song1",
      "artist": ["Blue"],
      "duration": 2.54
    },
    {
      "title": "song2",
      "artist": ["Kitty", "DJcat"],
      "duration": 5.25
    },
    {
      "title": "meow meow",
      "artist": ["Garfield"],
      "duration": 2.0
    }
  ]
}

total_length = 0
for song in playlist["songs"]:
  total_length += song["duration"]
  print(f'Song duration: { song["duration"] }')
print(f"Playlist time legth: {total_length}")

# Dictionary comprehension
square_numbers = { num: num ** 2 for num in range(1, 6)}
print(square_numbers)

states = ["California", "New Jersey", "Rhode Island"]
abbreviations = ["CA", "NJ", "RI"]
state_abbreviations = { abbreviations[i] : states[i] for i in range(0, len(abbreviations))} 
print(state_abbreviations)

capital_letters = { asciiCode: chr(asciiCode) for asciiCode in range(65, 91)}
print(capital_letters)

# DC with conditional logic
parity = {num: ("even" if num % 2 == 0 else "odd") for num in range (1, 10)}
print(parity)