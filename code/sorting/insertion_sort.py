def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]

        j = i - 1
        while numbers[j] > key and j >= 0:
            numbers[j + 1] = numbers[j]
            j = j - 1

        numbers[j + 1] = key

    return numbers


def _swap_array_values(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
