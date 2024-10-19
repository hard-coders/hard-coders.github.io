import pytest


class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()


@pytest.mark.parametrize(
    "example, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_solution(example, expected):
    solution = Solution()

    solution.reverseString(example)
    assert example == expected
