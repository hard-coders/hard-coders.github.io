---
date:
  created: 2024-10-13
categories:
  - leetcode
tags:
  - leetcode
  - palindrome

---

# 125. Valid Palindrome

## 문제

리트코드 [125번 문제](https://leetcode.com/problems/valid-palindrome/description/)입니다.

문자열이 주어졌을 때, 이 문자열이 [회문(palindrome)](https://ko.wikipedia.org/wiki/%ED%9A%8C%EB%AC%B8)인지 확인하는 문제입니다. 
대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 합니다.

<!-- more -->

문자열 `s`가 주어졌을 때, 회문이면 `true`를 그렇지 않으면 `false`를 반환해야 합니다.

## 풀이

파이써니스타라면 직관적으로 `reversed()`나 슬라이싱을 떠올렸을 겁니다. 
영문자 + 숫자 조합만 허용하므로 `str.isalnum()` 메소드와 리스트 컴프리헨션으로 문자열을 변환합니다.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
```

/// details | 테스트 코드
    type: success
    open: false

```python {linenums=1 hl_lines="3-6"}
import pytest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]

    
@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ],
)
def test_solution(s, expected):
    solution = Solution()

    assert solution.isPalindrome(s) is expected
```
///

시간 복잡도는 $O(n)$입니다.