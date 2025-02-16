arr = [100, 200, 130, 40, 2, 1, -1]


def min_and_max(arrays):
    minimum, maximum = arrays[0], arrays[0]

    for num in arrays[1:]:
        if minimum > num:
            minimum = num

        if maximum < num:
            maximum = num

    print("Minimum value is: ", minimum)
    print("Maximum value is: ", maximum)


min_and_max(arr)
