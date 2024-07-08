# TUPLES
alphabet = ('a', 'b', 'c', 'd')
print(type(alphabet))

# Commonly used for UNCHANGING DATA:
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# They can be used as keys in dictionaries:
locations = {
  (35.6895, 39.6917): 'Tokyo Office',
  (40.7128, 74.0060): 'New York Office',
  (37.7749, 122.4194): 'San Francisco Office'
}

# SETS
s = {1,2,3}
print(s)

# sets do not have duplicates
user_cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai", "Rosario", "Kyoto"]
print(list(set(user_cities)))

# Set union and intersection
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "James", "Oliver"}
students = math_students | biology_students
double_lecture_students = math_students & biology_students
print(students, double_lecture_students)

#Set comprehension
square = {x**2 for x in range(10)}
print(square)