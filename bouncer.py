age = input("How old are you? ");

if age:
  age = int(age)
  if age < 18:
    print("Come back when you're older")
  elif age < 21:
    print("I'm putting you on this NO ALCOHOL wristband, if you remove it you'll be kicked out")
  else:
    print("Come in!")

print('Hello?')