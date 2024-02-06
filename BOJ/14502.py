#first line
N, M = map(int, input().split())

arr = []
virus = []
wall_cand = set()


for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            wall_cand.add((i, j))

from itertools import combinations
from collections import deque
from copy import deepcopy

def test_with_three_walls(walls, original_arr):
    test_arr = original_arr

    for wall_x, wall_y in walls:
        test_arr[wall_x][wall_y] = 1
    
    
    # bfs
    q = deque()
    q.extend(virus)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * M for _ in range(N)]
    
    while q:
        x, y = q.popleft()
        
        test_arr[x][y] = 2
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and test_arr[nx][ny] == 0 and not visited[nx][ny]:
                q.append((nx, ny))
    
    # count
    count = 0
    for i in range(N):
        for j in range(M):
            if test_arr[i][j] == 0:
                count += 1


    for wall_x, wall_y in walls:
        test_arr[wall_x][wall_y] = 0
    
    return count
        
    
        
        

max_value = 0
for a,b,c in combinations(wall_cand, 3):
    max_value = max(max_value, test_with_three_walls((a,b,c), arr))
    

print(max_value)




