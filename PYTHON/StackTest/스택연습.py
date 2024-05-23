count = list()

def push(push_data) :
    count.append(push_data)

def pop() :
    count.remove(count[-1])

a = input()
print(a)

for i in a :
    if i =='(' :
        push(i)
        print("스택에 추가되는 과정 : {}".format(count))
    elif i ==')' :
        pop()
        print("스택에서 삭제된 결과 : {}".format(count))

if count == [] :
    print("스택이 비어있음 : OK")
else :
    print("스택이 비워지지 않음 : error")