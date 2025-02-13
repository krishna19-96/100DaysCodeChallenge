arr = [100, 200, 130, 40, 2, 1]


def reverse_an_array(arrays):
    for i in range(0, len(arrays) // 2):
        first = arrays[i]
        arrays[i] = arrays[len(arrays) - i-1]
        arrays[len(arrays) - i-1] = first

    print(arrays)


reverse_an_array(arr)
