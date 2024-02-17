from collections import defaultdict
import heapq as hq
from itertools import filterfalse


def solution(N, road, K):

    adj = defaultdict(list)
    for (
        a,
        b,
        c,
    ) in road:
        adj[a].append((b, c))
        adj[b].append((a, c))

    visited = defaultdict(bool)
    dist = defaultdict(lambda: float("inf"))

    # 초기화
    q = []
    dist[1] = 0
    hq.heappush(q, (0, 1))
    while q:
        d, u = hq.heappop(q)
        visited[u] = True

        for v, w in adj[u]:
            if not visited[v] and dist[v] > d + w:
                dist[v] = d + w
                hq.heappush(q, (dist[v], v))

    answer = len(list(filterfalse(lambda x: x > K, dist.values())))

    return answer


def main():
    sample_input = (
        5,
        [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]],
        3,
    )
    print(solution(*sample_input))


if __name__ == "__main__":
    main()
