from collections import deque
import queue

n, e, start_point = map(int, input().split())

# 인접 리스트
attach = [[] for _ in range(n+1)]

for _ in range(e):
    s, e = map(int, input().split())
    attach[s].append(s)
    attach[e].append(e)

# 인접 리스트 정렬
for i in range(n+1):
    attach[i].sort()

def DFS(i):
    visited = True
    print(i, end=' ')
    for node in attach[i]:
        if not visited[node]:
            DFS(node)

visited = [False] * (n+1)
DFS(start_point)
print()
def BFS(i):
    q = queue.Queue()
    q.put(i)
    visited = True

    while q:
        n = q.get()
        print(n, end=' ')
        for node in attach[n]:
            if not visited[node]:
                visited[node] = True
                q.put(node)

visited = [False] * (n+1)
BFS(start_point)