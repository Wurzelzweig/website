import math

user_input = float(input("Edge length: "))

surface = user_input ** 2 * math.sqrt(3)
volume = (user_input ** 3 / 12) * math.sqrt(2)
height = (user_input / 3) * math.sqrt(6)

surface = round(surface, 4)
volume = round(volume, 4)
height = round(height, 4)

print(f"Surface: {surface}")
print(f"Volume: {volume}")
print(f"Height: {height}")