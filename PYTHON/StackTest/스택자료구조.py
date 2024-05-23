abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

stack = list()

def push(push_data) :
    stack.append(push_data)

def pop() :
    print(stack[-1], end = " ")
    stack.remove(stack[-1])
    

    
print('+++삽입되는 순서+++')


for i in abcd :
    push(i)
    print(stack)

print('+++삭제되는 순서+++')

for i in range(len(stack)) :
    pop()

