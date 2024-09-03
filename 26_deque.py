from collections import deque

def DFS(i : int):
    print(i, end=' ')
    visited[i] = True

    for node in attach[i]:
        if not visited[node]:
            DFS(node)

def BFS(i : int):
    dq = deque()
    dq.append(i)
    visited[i] = True
    while dq:
        node = dq.popleft()
        print(node, end=' ')
        for n in attach[node]:
            if not visited[n]:
                visited[n] = True
                dq.append(n)
            
# 방문하는 노드가 여러개면 노드 번호 작은것부터 -> sort()
# 노드번호 1~N
# input = 노드 개수, 엣지 개수, 탐색 시작 노드
n, e, sn = map(int, input().split())

# 인접 리스트 초기화
attach = [[] for _ in range(n+1)]

# 인접 리스트 설정
for _ in range(e):
    start, end = map(int, input().split())
    attach[start].append(end)
    attach[end].append(start)

# 인접 리스트 정렬
for i in range(n+1):
    attach[i].sort()

# 방문 리스트 초기화
visited = [False] * (n+1)
DFS(sn)
print()

# BFS를 위해서 방문 리스트 초기화
visited = [False] * (n+1)
BFS(sn)