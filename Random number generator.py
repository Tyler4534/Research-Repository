import random
# First method of random number generator  
num = random.random()
print(num)

# Second method of random number generator 
number = random.randint(1,100)
print("\nThe random number is", number)

print()

# Third method of random number generator
list_numpick = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(random.choice(list_numpick))

