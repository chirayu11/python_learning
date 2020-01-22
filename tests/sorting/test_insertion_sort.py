from code.sorting.insertion_sort import insertion_sort


def test_insertion_sort_returns_correct_values():
    numbers = [6, 5, 4, 1, 2, 3]

    result = insertion_sort(numbers)

    assert result == sorted(numbers)
