test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d_places = int(input('Enter the d places: '))

# my code


def left_rotate_an_array(arrays, d):
    index = 0
    new_arr = arrays.copy()
    for i in range(d, len(arrays)):
        arrays[index] = arrays[i]
        index += 1

    for i in range(0, d):
        arrays[index] = new_arr[i]
        index += 1

    print(arrays)


left_rotate_an_array(test_data, d_places)


def left_rotate_an_array_with_inbuilt_methods(arrays, d):

    for i in range(d):
        value = arrays.pop(0)
        arrays.append(value)

    print(arrays)


left_rotate_an_array_with_inbuilt_methods(test_data, d_places)
