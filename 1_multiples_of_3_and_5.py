""" Find the multiples of 3 and 5 """

def multiples_of(m, below):
    total = 0
    for i in range(below):
        if i % m == 0:
            total += i
    return total


# Find all the multiples of 3 below 1000

print(f"For multiples of 3 below 10 the answer should be 18. It is: {multiples_of(3, 10)}")
print(f"For multiples of 3 below 1000 the answer is: {multiples_of(3, 1000)}")

# Find all the multiples of 5 below 1000

print(f"For multiples of 5 below 10 the answer should be 5. It is: {multiples_of(5, 10)}")
print(f"For multiples of 5 below 1000 the answer is: {multiples_of(5, 1000)}")


# Find all the multiples of 15 below 1000

# Add the 3 and 5s together and subtract the fifteens
below = 1000
answer = multiples_of(3, below) + multiples_of(5, below) - multiples_of(15, below)

# Return the answer
print(f"Below {below} the answer is: {answer}")
