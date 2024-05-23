coins = [500, 100, 50, 10]

n = int(input("지불할 돈을 입력해 주세요 : "))

coin500 = n // 500
n = n % 500
print("500원의 개수 : %d" % coin500)
print("500을 뺀 남은 액수 : %d" % n)

coin100 = n // 100
n = n & 100
print("100원의 개수 : %d" % coin100)
print("100을 뺀 남은 액수 : %d" % n)

coin50 = n // 50
n = n % 50
print("50원의 개수 : %d" % coin50)
print("50을 뺀 남은 액수 : %d" % n)

coin10 = n // 10
n = n & 10
print("10원의 개수 : %d" % coin10)
print("10을 뺀 남은 액수 : %d" % n)

coin_dic = {"500" : coin500, "100" : coin100, "50" : coin50, "10" : coin10}

print("따라서, 거스름돈은 동전별 각각", end = " ")
for key, value in coin_dic.items() :
    print(key, ":", value, end = " ")
print("개 지불하면 됩니다.")