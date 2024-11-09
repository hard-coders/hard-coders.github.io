---
date:
  created: 2024-11-09
categories:
  - 리트코드
tags:
  - 리트코드
  - 문자열
---

# 3. 중복 문자 없는 가장 긴 부분 문자열

## 문제

리트코드 [3번 문제](https://leetcode.com/problems/longest-substring-without-repeating-characters)입니다.

문자열 `s`가 주어졌을 때, 중복 문자가 없는 가장 긴 부분 문자열을 구하는 문제입니다.
응답은 부분 문자열이 아닌 부분 문자열의 크기를 반환하면 됩니다.


<!-- more -->

여기서 부분 문자열(substring)이란, 문자열의 연속한 어떤 부분을 의미합니다.
예를 들어, `pwwkew`에서 `pwke`는 중복 없는 가장 긴 부분 시퀀스(subsequence)이고,
`wke`가 가장 긴 부분 문자열입니다.

## 풀이

순차적으로 진행하면서 부분 문자열의 최대 길이를 구하고, 새로운 문자가 등장하면 부분 문자열을 다시 시작하면 될 거 같습니다.

책에 있는 그림(11-10)을 표현 해보면,

```
s = | a | b | c | a | b | c | b | b |
    |-->|   |   |   |   |   |   |   |
    | 1 |   |   |   |   |   |   |   |
    |---|-->|   |   |   |   |   |   |
    |   | 2 |   |   |   |   |   |   |
    |---|---|-->|   |   |   |   |   |
        |   | 3 |   |   |   |   |   |
        |---|---|-->|   |   |   |   |
            |   | 3 |   |   |   |   |
            |---|---|-->|   |   |   |
                |   | 3 |   |   |   |
                |---|---|-->|   |   |
                        | 3 |   |   |
                        |---|-->|   |
                            | 2 |   |
                            |---|-->|
                                | 1 |
```
화살표 _끝_ 은 그저 순차적으로 진행합니다.
한 칸 전진 할 때마다 최대 길이(`max_len`)을 구해줍니다.

만약 기존에 봤던 문자가 다시 등장하면 화살표의 _시작_(`start`라고 합시다)을 한 칸 전진 합니다.

`start = 봤던 문자 위치 + 1`이 됩니다.

여기서 화살표는 보통 윈도우(window)라고 부르고, 미끄러지면서(sliding) 이동하기 때문에
슬라이딩 윈도우라 부릅니다.


위치가 갱신되었기 때문에 최대 길이를 다시 구할 필요 없습니다.
아래는 구현 코드입니다.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = start = 0

        for i, c in enumerate(s):
            # 문자(c)를 전에 봤다면, start를 봤던 문자에서 한 칸 전진하여 새로운 부분 문자열 시작
            if c in seen:
                start = seen[c] + 1
            else:
                max_len = max(max_len, i - start + 1)

            # 봤던 문자의 위치를 기록합니다.
            seen[c] = i

        return max_len
```

/// note
문제풀이 할 때 투 포인터를 사용할 경우 `left`, `right`라는 변수명을 자주 사용합니다.
손으로 그림을 그릴때도 명확해서 이해하기 쉽기 때문입니다.
위에서는 `start`가 `left`이고 `i`가 `right`입니다. 서두의 그림을 보면서 대입해보면 정말 편합니다.
///

그런데 리트코드에 제출하면 다음 케이스에서 실패합니다.

```python
s = "tmmzuxt"
```

왜냐하면, 봤던 문자(여기서는 `t`)가 마지막에 있을때 `else`문을 안 타고 `if`문을 타서 최댓값을 안 구하기 때문입니다.
`mzuxt`가 되어야하는데 `t`가 재등장해 `mzux`가 되고 `for` 루프가 끝나 종료됩니다. 

다른 말로 윈도우 밖에 있는 문자는 예전에 봤더라도 무시해야 합니다.
`if`에 `start <= seen[c]` 조건을 추가해 코드를 완성합시다.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = start = 0

        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                max_len = max(max_len, i - start + 1)

            seen[c] = i

        return max_len
```


/// details | 테스트 코드
    type: success
    open: false

```python {linenums=1 hl_lines="4-17"}
import pytest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_len = start = 0

        for i, c in enumerate(s):
            if c in seen and start <= seen[c]:
                start = seen[c] + 1
            else:
                max_len = max(max_len, i - start + 1)

            seen[c] = i

        return max_len


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # abc
        ("bbbbb", 1),  # b
        ("pwwkew", 3),  # wke
        ("tmmzuxt", 5),  # mzuxt
    ],
)
def test_solution(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected
```
///

시간 복잡도는 순차탐색만 했으므로 $O(n)$입니다.
