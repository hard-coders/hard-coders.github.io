---
date:
  created: 2024-10-28
categories:
  - 리트코드
tags:
  - 리트코드
  - 카데인
---

# 121. 주식을 사고 팔기 가장 좋은 때

## 문제

리트코드 [121번 문제](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)입니다.

`i`번째 날의 주식가가 있는 `prices` 리스트를 받아 최대 이익을 구하는 문제입니다.

<!-- more -->

워렌 버핏의 유명한 말을 알고리즘으로 구현하면 됩니다.

> Buy the fear, sell the greed
> 
> 워렌 버핏

~~쌀 때 사서 비쌀때 파는게 아닌거 같은데?~~

## 풀이

`profit`을 최대로 잡아야하는데, 그럴 수 없다면 문제에서 0을 반환하라 되어있습니다.

`profit`을 `0`으로, `min_price`를 무한으로 선언하고 리스트를 탐색하면서 최저가를 찾아 넣으면 됩니다.

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
```


/// info | 무한대
최소, 최대를 비교할 때 무한대를 활용하면 편합니다. `None`을 사용할 경우 타입 에러가 날 수 있습니다.
또는 임의로 999,999,999와 같이 할 경우 테스트 케이스가 이보다 클 수 있습니다.
무한을 선언하는 방법은 `math.inf`, `float("inf")`, `Decimal("inf")` 등이 있습니다.

책에서는 `sys.maxsize`를 활용해 시스템 상 가장 큰 수를 이용해 비교합니다.
///

/// details | 테스트 코드
    type: success
    open: false

```python {linenums=1 hl_lines="4-12"}
import pytest


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = float("inf")

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_solution(prices, expected):
    solution = Solution()
    assert solution.maxProfit(prices) == expected

```
///

## 시간 복잡도

단순히 한 번만 탐색하므로 시간 복잡도는 $O(n)$입니다.
