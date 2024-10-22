---
date:
  created: 2024-10-23
categories:
  - 리트코드
tags:
  - 리트코드
  - 회문
  - 문자열
  - 부분 문자열
draft: true
---

# 5. Longest Palindrome Substring

## 문제

리트코드 [5번 문제](https://leetcode.com/problems/longest-palindromic-substring/)입니다.

주어진 문자열에서 가장 긴 회문을 찾아 반환합니다.

<!-- more -->

## 풀이

투 포인터를 활용하여 회문을 찾습니다. 회문은 홀수와 짝수의 경우로 나누어 생각할 수 있습니다.

1. 홀수, 짝수 길이의 회문을 찾습니다.
2. 두 경우 중 가장 긴 회문을 반환합니다.
3. 회문을 찾는 함수를 만들어 풀이합니다.
4. 회문을 찾는 함수는 주어진 문자열과 시작, 끝 인덱스를 받아 회문을 찾습니다.


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
```

/// details | 테스트 코드
    type: success
    open: false
```python {linenums=1 hl_lines="4-18"}
import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result


@pytest.mark.parametrize(
    "s, expected",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
    ],
)
def test_solution(s, expected):
    solution = Solution()
    assert solution.longestPalindrome(s) == expected
```
///

- `expand` 함수는 주어진 문자열과 시작, 끝 인덱스를 받아 회문을 찾습니다.
- `s`의 길이가 2보다 작거나, `s`가 회문이라면 `s`를 반환합니다.
- `result` 변수에 가장 긴 회문을 저장합니다.
- `s`의 길이 - 1까지 반복하며, `expand` 함수를 호출하여 가장 긴 회문을 찾습니다.
- `expand` 함수는 `i`와 `i + 1`, `i`와 `i + 2`를 비교하여 가장 긴 회문을 찾습니다.
- `max` 함수를 이용해 가장 긴 회문을 찾습니다.
- `key=len`을 이용해 길이가 가장 긴 회문을 반환합니다.

## 시간 복잡도

`expand` 함수는 최악의 경우 $O(n)$의 시간 복잡도를 가집니다.
해당 함수를 이용하여 가장 긴 회문을 찾으므로, 전체 시간 복잡도는 $O(n^2)$입니다.

