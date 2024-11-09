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
---

# 5. 가장 긴 회문 부분 문자열

## 문제

리트코드 [5번 문제](https://leetcode.com/problems/longest-palindromic-substring/)입니다.

주어진 문자열에서 가장 긴 회문을 찾아 반환합니다.

<!-- more -->

## 풀이

투 포인터를 활용하여 회문을 찾습니다. 회문은 홀수(포인터1)와 짝수(포인터2)의 경우로 나누어 생각할 수 있습니다.
회문을 찾는 함수는 해당 문자에서 왼쪽, 오른쪽으로 확장하는 함수를 만들면 됩니다. 아래 예시를 보면 이해가 조금 수월 할 겁니다.

만약 `s`가 `babad`라면,

* `i = 0`: `"b"abad`
  > * 홀
  >> * `[b]abad` ✅ 
  > * 짝
  >> * `[ba]bad` ❌
* `i = 1`: `b"a"bad`
  > * 홀
  >> * `b[a]bad` ✅
  >> * `[bab]ad` ✅ 정답입니다.
  > * 짝
  >> * `b[ab]ad` ❌
* `i = 2`: `ba"b"ad`
  > * 홀
  >> * `ba[b]ad` ✅
  >> * `b[aba]d` ✅ 역시 정답입니다.
  >> * `[babad]` ❌
  > * 짝
  >> * `ba[ba]d` ❌
* `i = 3`: `bab"a"d`
  > * 홀
  >> * `bab[a]d` ✅
  >> * `ba[bad]` ❌
  > * 짝
  >> * `bab[ad]` ❌
* `i = 4`: `baba"d"`: 짝수일 경우 오버플로우이므로 패스합니다.

위 예에서는 `i`가 1일 때, `bab`와 2일 때, `aba` 가 가장 깁니다. 리트코드에서는 둘 모두 정답으로 처리합니다.

1. 홀수, 짝수 길이의 회문을 찾습니다.
2. 두 경우 중 가장 긴 회문을 반환합니다.
3. 포인터를 오른쪽으로 이동합니다.


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 한 글자는 자기 자신으로 회문입니다. 그리고 자기 자신을 뒤집은게 같다면 역시 회문입니다.
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
```

`if` 문이 있는 이유는 최선, 최악의 경우 바로 정답을 알 수도 있지만, `expand` 함수에서 인덱스 오버플로우가 나지 않기 위함도 있습니다.

/// details | 테스트 코드
    type: success
    open: false
```python {linenums=1 hl_lines="4-18"}
import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

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

## 시간 복잡도

`expand` 함수는 최악의 경우 $O(n)$의 시간 복잡도를 가집니다.
해당 함수를 이용하여 가장 긴 회문을 찾으므로, 전체 시간 복잡도는 $O(n^2)$입니다.

