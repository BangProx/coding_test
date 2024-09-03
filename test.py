from collections import deque
import queue

dq = deque()

dq.append(1)
dq.append(2)
dq.append(3)

print(dq)

print(dq.pop())


# FIFO Queue 생성
q = queue.Queue()

# 큐에 항목 추가
q.put(1)
q.put(2)
q.put(3)

# 큐에서 항목 꺼내기
print(q.get())  # 1 출력
print(q.get())  # 2 출력
print(q.get())  # 3 출력