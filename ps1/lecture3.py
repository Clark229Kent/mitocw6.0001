"""cube = 8
for guess in range (0,abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = - guess
    print("Cube root of " + str(cube) + " is " + str(guess))"""

cube = 7
epsilon = 0.01
guess = 0.0
increment = 0.001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("num_guesses =", num_guesses)
if abs(guess**3-cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess,"is close to the cube root of", cube)
