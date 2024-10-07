# todo: Данные две переменные:
# age = 36.6
# temperature = 25
# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:

age = 36.6
temperature = 25

transit = age
age = temperature
temperature = transit
print(f'Hello, my age is {age} years old, my temperature is {temperature} degrees')