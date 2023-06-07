def revers_range(num):
    if num > 0:
        revers_range(num-1)
    print(num, end="")
