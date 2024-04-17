# Richard Partridge
# Python Arrays

import numpy as np

# Create a 2-dimensional 5 by 5 array with random numbers
rando_nump = np.random.randint(1, 100, size=(5, 5), dtype=int)

# Print the entire array.
print("Here is a 5 by 5 array of random numbers:")
print(rando_nump)

# Print the number from the 2nd row, 3rd column
print("\nThe number from the 2nd row, 3rd column is:")
print(rando_nump[1, 2])

# Print the sum of all the elements in the array.
print("\nThe sum of all the elements in the array is:")
print(np.sum(rando_nump))

# Print the mean of each row in the array.
print("\nThe mean of each row in the array is:")
print(np.mean(rando_nump, axis=1))

# Print the maximum value in each column of the array.
print("\nThe maximum value in each column of the array is:")
print(np.max(rando_nump, axis=0))
