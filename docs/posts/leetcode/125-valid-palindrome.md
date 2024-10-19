---
date:
  created: 2024-10-13
categories:
  - programming
  - leetcode
tags:
  - leetcode
  - leetcode125
  - palindrome
---

# Leetcode 125. Valid Palindrome

## Overview

문자열이 주어졌을 때, 이 문자열이 palindrome인지 확인하는 문제입니다. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 합니다.



```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
```

///// details | 테스트 코드
    type: tip
    open: false

as-is 코드이므로 바로 실행 가능합니다.

//// details | `pytest`가 없다면 설치하세요!
    type: check
    open: false
`pytest`는 테스트 코드를 실행하는 데 사용되는 라이브러리입니다. 설치가 되어 있지 않다면 아래 명령어를 통해 설치하세요.

/// tab | pip
```shell
pip install pytest
```
///

/// tab | poetry
```shell
poetry add pytest
```
///

/// tab | uv
```shell
uv add pytest
```
///

////

```python {title="125_valid_palindrome.py" linenums=1}
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
/////

아아아 일단 일케 일케 하나씩 해보자



