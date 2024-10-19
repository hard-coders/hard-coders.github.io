---
date:
  created: 2024-10-10
categories:
  - leetcode
tags:
  - leetcode
---

# 리트코드 풀이

## 머릿말

이 문서는 리트코드 문제를 풀고 풀이를 정리한 문서입니다. 모든 문제는 파이썬으로 풀이하며, 테스트 코드를 작성하여 검증합니다.

풀이는 [박상길, "파이썬 알고리즘 인터뷰", 책만(2020)](https://github.com/onlybooks/python-algorithm-interview) 책을 참고하여 작성하였습니다.

개인적으로 정리하는 포스팅이므로 개인적인 풀이나 커트텀이 있을 수 있습니다. 또한 모든 풀이를 쓰지 않았습니다.
직접 책을 구매하시길 **강력 추천**합니다. 오랫동안 알고리즘을 잊고 지냈는데 이 책을 보고 다시 공부하니 친절한 설명과 그림 덕분에 이해가 잘 되어 정말 좋았습니다.

취업준비생 뿐만 아니라, 저처럼 한동안 알고리즘을 놓고 지내신 분들 모두에게 추천합니다.

## 테스트 코드

각 문제 풀이마다 아래와 같이 테스트 코드를 작성하고 있습니다.

/// details | 테스트 코드
    type: tip
    open: false

모든 코드는 복사 후 붙여넣기 시 바로 실행 가능합니다.
///

테스트 코드는 `pytest`를 사용합니다. 없다면 아래 도구 중 하나를 이용하여 설치하세요.

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
# 또는 설치 없이 바로 실행하려면
uvx pytest
```
///