# 다 검색 했음

fiboCount = 0
fibCount = 0

# 재귀
def fibo(n) :
    global fiboCount
    fiboCount += 1

    if n==1 or n==2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
    

# DP
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(탑다운 DP)
def fib(x):
    global fibCount
    fibCount += 1
	# 종료 조건
    if x == 1 or x == 2:
    	return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
    	return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

print("## 30번째 피보나치 수열 ##")
print("재귀 방식 --> 답: ", fibo(31), "반복수 : ", fiboCount)
print("DP 방식 --> 답: ", fib(31),  "반복수 : ", fibCount)
