from code.recursion.recursion import generate_all_subsets, get_all_valid_parentheses_pairs, queens


def test_generate_all_subsets_works():
    input = [1,2,3,5,6,7,8,9,10]
    output = generate_all_subsets(input)

    assert len(output) == 2 ** len(input)


def test_get_all_valid_parentheses_pairs_works():
    output = get_all_valid_parentheses_pairs(4)

    assert len(output) == 13


def test_queens_works():
    output = queens(8)

    assert len(output)
