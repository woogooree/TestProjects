LSearch_list = [12, 10, 27, 51, 7, 96]
print(LSearch_list)

i = 0

search = int(input("당신이 찾고자 하는 수를 입력 : "))

# while i < len(LSearch_list) :
#     print(f'index {i} : ', LSearch_list[i])
#     if LSearch_list[i] == search :
#         print(f'인덱스[{i}]에서 탐색 성공')
#         print('탐색 종료')
#         break
#     else :
#         i += 1

for i in range (0, len(LSearch_list)) :
    print(f'index {i} : ', LSearch_list[i])
    if LSearch_list[i] == search :
        print(f'인덱스[{i}]에서 탐색 성공')
        print('탐색 종료')
        break



LSearch_list = list()

for i in range(5) :
    num = int(input("입력값 : "))
    LSearch_list.append(num)

print("리스트 = ", LSearch_list)

search = int(input("찾고자 하는 수 : "))
for idx in range(0, len(LSearch_list)) :
    print(f'index {idx} :', LSearch_list[idx])
    if LSearch_list[idx] == search :
        print(f'인덱스[{idx}]에서 탐색 성공')
        print("탐색 종료")
        break