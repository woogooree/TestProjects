import sys
input = sys.stdin.readline

N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N) :
    find = A[k]
    i = 0
    j = N - 1
    while i < j and i < N and j >= 0 :
        if A[i] + A[j] == find :
            if i != k and j !=k :
                Result += 1
                break
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif A[i] + A[j] < find :
            i += 1
        else :
            j -= 1
print(Result)


N = int(input())
A = [0]*N

for i in range(N) :
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N) :
    su = A[i]
    if su >= num :
        while su >= num :
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else :
        n = stack.pop()

        if n > su :
            print("NO")
            result = False
            break
        else :
            answer += "-\n"
    if result :
        print(answer)

from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1) :
    myQueue.append(i)

while len(myQueue) > 1 :
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])    




arr = [40, 70, 60, 30, 10, 50]
for i in range(len(arr)-1) :

    small_idx = i

    for j in range(i + 1, len(arr)) :
        if arr[small_idx]>arr[j] :
            small_idx = j
    arr[i],arr[small_idx] = arr[small_idx],arr[i]
print(arr)            



for i in range(len(arr)-1, 0, 1) :
    for j in range(i) :
        if arr[j] > arr[j+1] :
            arr[j],arr[j+1] = arr[j+1],j[j]

print(arr)



arr = [40, 60, 70, 50, 10, 20, 30]

for i in range(1,len(arr)) :
    for j in range(i, 0, -1) :
        if arr[j-1] > arr[j] :
            arr[j],arr[j-1] = arr[j-1],arr[j]

arr = [40, 70, 60, 30, 10, 50, 90, 80, 20]

def big_heap(a,b) :
    for i in range(1,b+1) :
        c = i
        while c != 0 :
            r = (c-1) // 2
            if a[r] < a[c] :
                a[r],a[c] = a[c],a[r]
            c=r    


