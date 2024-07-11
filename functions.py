from random import random

def exponent(num, power=2):
  return num**power

print(exponent(7)) # positional argument + default value
print(exponent(power=3, num=2)) # keyword arguments -> order doesn't matter

def flip_coin():
  """A simple function that imitates a coin flip"""
  if random() > 0.5:
    return 'heads'
  else:
    return 'tails'

print(flip_coin())
print(flip_coin())
print(flip_coin())

def day(num):
  days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
  return days.get(num)

print(day(1))

def single_letter_count(string,letter):
  return string.lower().count(letter.lower())

print(single_letter_count("Amazing!", "a"))

def sum_all_values(*args):
  total = 0
  for val in args:
    total += val
  return total

print(sum_all_values(1,34,65,3))
nums = (32,5,43,87)
print(sum_all_values(*nums)) # unpacking lists and tuples

def fav_colors(**kwargs):
  for person, color in kwargs.items():
    print(f"{person}'s favourite color is {color}")

fav_colors(Colt='purple', Ruby="red", Ethel='teal')
favourite_colors = { "Amanda": "green", "Yolanda": "black"}
fav_colors(**favourite_colors) # unpacking dictionaries