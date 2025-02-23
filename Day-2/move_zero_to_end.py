test_data = [0, 1, 2, 0, 3, 4, 5]


def move_zero_to_end_with_inbuilt_methods(arrays):
    if len(test_data) > 1:
        for i in range(len(test_data)):
            if test_data[i] == 0:
                zero_index = test_data.pop(i)
                test_data.append(zero_index)

        print(test_data)
    else:
        print("Array length is lesser than one")


move_zero_to_end_with_inbuilt_methods(test_data)


def move_zero_to_end(arrays):
    index = 0
    new_array = [0] * len(arrays)
    if len(test_data) > 1:
        for i in range(0, len(test_data) - 1):
            if test_data[i] > 0:
                new_array[index] = test_data[i]
                index += 1

        print(new_array)


move_zero_to_end(test_data)
