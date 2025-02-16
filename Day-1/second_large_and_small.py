arr = [100, 7, 9, 1, -1, 2, 20]


def second_large_and_small(arrays):
    min1, min2 = arrays[0], arrays[0]
    max1, max2 = arrays[0], arrays[0]
    for num in arrays[1:]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num > min1 and (num < min2 or min1 == min2):
            min2 = num

        if num > max1:
            max2 = max1
            max1 = num
        elif num < max1 and (num > max2 or max1 == max2):
            max2 = num

    print("Second Smallest no is : ", min2)
    print("Second Largest no is : ", max2)


second_large_and_small(arr)


