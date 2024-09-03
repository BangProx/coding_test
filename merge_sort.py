import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s,e):
    if e - s < 1: return
    m = int(s + (e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)

    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            