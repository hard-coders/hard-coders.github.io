import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:  # noqa
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]


@pytest.mark.parametrize(
    "example, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_solution(example, expected):
    solution = Solution()

    assert solution.isPalindrome(example) is expected
