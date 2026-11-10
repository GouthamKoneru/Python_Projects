def recursive_countdown(number):
    if number < 1:
        return
    print(number)
    recursive_countdown(number - 1)
    print(number)
recursive_countdown(9)