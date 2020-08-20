class Solution:
    def isHappy(self, n: int) -> bool:
        numbers_created = {}
        current_number = n
        while current_number != 1:
            if current_number in numbers_created:
                return False
            numbers_created.add(current_number)
            next_number = self._get_next_number(current_number)
            current_number = next_number
            print(numbers_created)

        return True

    def _get_next_number(self, n: int) -> int:
        digit_list = [int(d) for d in str(n)]
        sum_of_squares = sum(map(lambda x: x ** 2, digit_list))
        return sum_of_squares

def test_solution_works():
    s = Solution()

    s.isHappy(19)