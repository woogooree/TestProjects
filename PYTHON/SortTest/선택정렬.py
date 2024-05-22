arr = [40, 70, 60, 30, 10, 50]
print(f'선택정렬 전 : {arr}')
print("+"*40)
for i in range(len(arr)-1) :
    min_idx = i
    for j in range(min_idx + 1, len(arr)) :
        if arr[j] < arr[min_idx] :
            min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f'{i+1}단계: {arr}')

print("+"*40)
print(f'선택정렬 결과 : {arr}')