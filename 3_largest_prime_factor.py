

def lpf(targ):
    i = 2
    factor_list = []

    # Find all the factors of the target
    print(f"Finding factors of {targ}.")
    while True:
        if targ % i == 0:
            factor_list.append(targ // i)
        if i >= targ // 2:
            break
        i = i + 1
    print(f"The factor list is {factor_list}")

    # Pull out the prime factors
    print(f"Finding prime factors of {targ}.")
    focus_index = 0
    max_index = len(factor_list)
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


target = 80
print(f"The largest prime factor of target: {target} is: {lpf(target)}")
print(f"EXPECT: the largest prime factor of target: 80 is: 5")
target = 13195
print(f"The largest prime factor of target: {target} is: {lpf(target)}")
print(f"EXPECT: the largest prime factor of target: 13195 is: 29")
target = 600851475143
print(f"The largest prime factor of target: {target} is: {lpf(target)}")

