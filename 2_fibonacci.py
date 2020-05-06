# Sum the e
a = 1
b = 1
c = 0
total = 0


while True:
    c = a + b

    if c > 4000000:
        break

    print(f"a: {a}, b: {b}, c: {c}")

    a = b
    b = c
    
    # Check if c is even
    if c % 2 == 0:
        total = total + c


print(f"total: {total}")

