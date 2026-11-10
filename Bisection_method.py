def square_root_bisection(square_target, tolerance=0.01, maximum=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)

    for _ in range(maximum):
        mid = (low + high) / 2

        if high - low <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid

        if mid ** 2 < square_target:
            low = mid
        else:
            high = mid

    print(f"Failed to converge within {maximum} iterations")
    return None