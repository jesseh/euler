
def list_factors(targ):
    """List all the factors for the target"""
    print(f"Finding factors of {targ}.")

    i = 2
    factor_list = []
    if targ % 2 == 0:
        factor = targ // 2
        factor_list.append(factor)
        factor_list.append(2)
        print(f"-> {factor} * {2}")
    denominator = (x for x in range(3,targ // 2, 2) if x%5)
    for x in denominator:
        if targ % x == 0:
            factor = targ // x
            factor_list.append(factor)
            factor_list.append(x)
            print(f"-> {factor} * {x}")
            if x > factor:
                break
    return sorted(factor_list, reverse=True)


def lowest_prime_factor(targ):
    factor_list = list_factors(targ)
    print(f"The factor list is {factor_list}")

    # Pull out the prime factors
    print(f"Finding prime factors of {targ}.")
    max_index = len(factor_list)
    focus_index = 0
    while focus_index < max_index:
        check_index = focus_index + 1
        while check_index < max_index:
            # print(f"Comparing {factor_list[focus_index]} to {factor_list[check_index]}")
            focus = factor_list[focus_index]
            check = factor_list[check_index]
            if focus % check == 0:
                break
            check_index = check_index + 1
            if check_index == max_index:
                return focus
        focus_index = focus_index + 1
    print("Error - no prime factors found")
    print("----------")


target = 80
print(f"The largest prime factor of target: {target} is: {lowest_prime_factor(target)}")
print(f"EXPECT: the largest prime factor of target: 80 is: 5")
target = 13195
print(f"The largest prime factor of target: {target} is: {lowest_prime_factor(target)}")
print(f"EXPECT: the largest prime factor of target: 13195 is: 29")
target = 600851475143
print(f"The largest prime factor of target: {target} is: {lowest_prime_factor(target)}")

