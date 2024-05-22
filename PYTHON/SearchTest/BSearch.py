BSearch_list = [7, 10, 12, 25, 27, 96, 1004]

search = 12
low = 0
high = 0
count = 0

while low <= high :
    middle = int((low + high) / 2)

    if search == BSearch_list[middle] :
        count += 1
        print(f'주어진 리스트에서 인덱스[{middle}]위치의 값인 {search}를 총 {count}번 만에 검색성공')
        print('탐색종료')
        break

    elif search > BSearch_list[middle] :
        low = middle + 1
        count += 1

    else :
        high = middle - 1
        count += 1