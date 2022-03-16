from collections import namedtuple
from enum import IntEnum
from typing import List, Tuple


class Direction(IntEnum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3


DirectionGuide = namedtuple("DirectionGuide", ["dir", "xd", "yd"])

order: Tuple[DirectionGuide] = (
    DirectionGuide(dir=Direction.EAST, xd=1, yd=0),
    DirectionGuide(dir=Direction.WEST, xd=-1, yd=0),
    DirectionGuide(dir=Direction.SOUTH, xd=0, yd=-1),
    DirectionGuide(dir=Direction.NORTH, xd=0, yd=1),
)


def findFourDirDFS(
    currentX: int,
    currentY: int,
    leftStep: int,
    probs: List[int],
    visited: List[List[bool]],
):
    if leftStep == 0:
        # 더이상 갈 수 있는 곳이 없으므로 여기서 종결 => 재귀 종료 조건
        return 1

    sumCases = 0
    for guide in order:
        if probs[guide.dir] == 0.0:
            continue
        newX = currentX + guide.xd
        newY = currentY + guide.yd

        if visited[newX][newY]:
            continue

        visited[newX][newY] = True
        sumCases += probs[guide.dir] * findFourDirDFS(
            newX, newY, leftStep - 1, probs, visited
        )

        visited[newX][newY] = False

    return sumCases


def main():
    inputs = list(map(int, input().split()))
    N = inputs[0]
    probs = list(map(lambda x: x / 100, inputs[1:]))
    visited = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
    visited[N][N] = True
    print(findFourDirDFS(N, N, N, probs, visited))


main()
