
# Problem 8.4: Power Set: Write a method to return all subsets of a set.
def generate_all_subsets(items):
    if not items:
        return [[]]
    elif len(items) == 1:
        return [[], items]

    subsets_ = generate_all_subsets(items[:-1])
    result = subsets_ + [sub + [items[-1]] for sub in subsets_]
    return result

# --------------------------------------------------------------------------------------

# Problem 8.9: Implement an algorithm to print all valid (e.g. properly open and closed)
# combinations of n pairs of parentheses.
# Input 3
# Output ((())), (()()), (())(), ()(()), ()()()
def get_all_valid_parentheses_pairs(number):
    if number == 1:
        return ['()']
    elif number == 2:
        return ['()()', '(())']

    one_less_result = get_all_valid_parentheses_pairs(number-1)
    result = set()
    for ans in one_less_result:
        result.add(ans + '()')
        result.add('()' + ans)
        result.add('(' + ans + ')')

    print(list(result))
    return list(result)


# --------------------------------------------------------------------------------------

# Problem 8.12: Eight queens - write an algorithm to print all ways of arranging eight queens on
# an 8x8 chess board so that none of them share the same row, column or diagonal. In this case,
# "diagonal" means all diagonals not just the two that bisect the board.
def queens(board_size):
    solutions = _queens_helper(board_size, [])
    print("Len {} Final solution {}".format(len(solutions), solutions))
    return solutions


def _queens_helper(board_size, queen_positions):
    if len(queen_positions) == board_size:
        return queen_positions

    solutions = []
    possibles = [(len(queen_positions), i) for i in range(board_size)]
    queen_position_possibles = _get_possibles_that_can_be_queen_positions(possibles, queen_positions)

    for candidate in queen_position_possibles:
        new_queen_positions = queen_positions + [candidate]
        more_solutions = _queens_helper(board_size, new_queen_positions)
        if more_solutions:
            solutions = solutions + [more_solutions]

    return solutions


def _get_possibles_that_can_be_queen_positions(possibles, queen_positions):
    ans = []
    queen_rows = set([i for i, _ in queen_positions])
    queen_cols = set([j for _, j in queen_positions])
    for possible in possibles:
        if possible[0] in queen_rows or possible[1] in queen_cols:
            continue

        queens_on_the_diagonal = _get_queens_on_the_diagonal(possible, queen_positions)

        if not queens_on_the_diagonal:
            ans.append(possible)
            
    return ans


def _get_queens_on_the_diagonal(possible, queen_positions):
    ans = []
    for queen_position in queen_positions:
        if abs(queen_position[0] - possible[0]) == abs(queen_position[1] - possible[1]):
            ans.append(queen_position)

    return ans
