def select_sort(arr) :
    min_idx = 0
    print(f'선택정렬 전 : {arr}')
    for i in range(len(arr)-1) :
        min_idx = i
        print(f'인덱스[{min_idx}]의 값인 {arr[min_idx]}의 {arr[min_idx]}의 위치', end='->')
        for j in range(min_idx + 1, len(arr)) :
            if arr[j] < arr[min_idx] :
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'배열에서 가장 작은 값인 {arr[i]}위치[{min_idx}]와 변경')
        print(f'인덱스[{i}]단계 교환 후 결과 : {arr}')
        print()
    print("="*70)
    print(f'선택 정렬된 이후 : {arr}')

    array = [40, 70, 60, 30, 10, 50]
    select_sort(array)
    