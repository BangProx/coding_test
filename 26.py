from collections import deque
n, e, start_point = map(int, input().split())

# 인접 리스트
attach = [[] for _ in range(n+1)]

# 인접 리스트 설정
for _ in range(e):
    s, e = map(int,input().split())
    attach[s].append(e)
    attach[e].append(s)

# 인접 리스트 정렬
for i in range(n+1):
    attach[i].sort()

def DFS(i):
    visited[i] = True
    print(i, end=' ')
    for node in attach[i]:
        if not visited[node]:
            DFS(node)

# 방문 리스트
visited = [False] * (n+1) 
DFS(start_point)

def BFS(i):
    dq = deque()
    dq.append(i)
    visited[i] = True

    while dq:
        n = dq.popleft()
        print(n, end=' ')
        for node in attach[n]:
            if not visited[node]:
                visited[node] = True
                dq.append(node)
print()
visited = [False] * (n+1)
BFS(start_point)
