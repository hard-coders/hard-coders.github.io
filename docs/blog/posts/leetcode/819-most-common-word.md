---
date:
  created: 2024-10-19
categories:
  - 리트코드
tags:
  - 리트코드
  - 카운터
---

# 819. 가장 흔한 단어

## 문제

리트코드 [819번 문제](https://leetcode.com/problems/most-common-word/)입니다.

문자열 `paragraph`와 금지된 단어 배열 `banned`가 주어질 때, 금지된 단어(`banned`)가 아닌 가장 빈번한 단어를 반환합니다. 적어도 하나의 금지된 단어가 아니며, 답은 유일합니다.

`paragraph`의 단어는 대소문자를 구분하지 않으며, 답은 소문자로 반환해야 합니다.

<!-- more -->

## 풀이

역시나 파이써니스타라면 `collections.Counter`를 떠올렸을 겁니다.

친절하게도 `paragraph`를 소문자로 반환하게 하여 대소문자를 구분하지 않도록 했습니다. 간단하게 다음과 같이 생각할 수 있습니다.

1. `paragraph`를 소문자로 변환합니다.
2. `paragraph`를 정규식을 이용해 단어로 분리합니다.
3. `banned`에 포함되지 않은 단어만 필터링합니다.
4. `collections.Counter`로 단어의 빈도수를 계산합니다.

/// tip | import 생략
리트코드 사이트에서는 `re`와 `collections` 모듈을 import하지 않아도 됩니다.
사이트 내에서는 보이지 않지만 이미 자주 쓰이는 모듈들이 포함되어 있기 때문입니다.
///

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [
            w for w in re.findall(r"\w+", paragraph.lower()) if w not in banned
        ]
        counter = Counter(words)
        return counter.most_common(1)[0][0]
```

/// details | 테스트 코드
    type: success
    open: false

```python {linenums=1 hl_lines="7-13"}
import re  # 리트코드에서는 불필요
from collections import Counter  # 리트코드에서 불필요

import pytest


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [
            w for w in re.findall(r"\w+", paragraph.lower()) if w not in banned
        ]
        counter = Counter(words)
        return counter.most_common(1)[0][0]


@pytest.mark.parametrize(
    "paragraph, banned, expected",
    [
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
        ("a.", [], "a"),
        ("Bob. hIt, baLl", ["bob", "hit"], "ball"),
    ],
)
def test_solution(paragraph, banned, expected):
    solution = Solution()
    assert solution.mostCommonWord(paragraph, banned) == expected
```
///

1~3번 과정은 한 줄로 처리할 수 있습니다. `collections.Counter`는 `most_common` 메서드를 통해 가장 빈번한 요소를 반환합니다.

/// tip | 정규식
정규식 `r"\w+"`은 단어를 찾는 패턴입니다. `\w`는 단어 문자를 의미하며, `+`는 1회 이상 반복을 의미합니다.
///



## 시간 복잡도

문자열을 정규식을 이용해 단어로 분리하고, `banned`에 포함되지 않은 단어만 필터링하므로 $O(n)$입니다.
