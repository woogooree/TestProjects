a = 10
b = 10
c = a + b
print(c)

c = 20
d = '10'

print(c + int(d))
print(str(c) + d)

e = 3.14
f = 10

print(e+f)
c = float(a) + float(b)
print(c)

a_bool = True
b_bool = False
a_int = 1
b_int = 0
print(a_bool)
print(b_bool)
print(type(a_bool))
print(type(b_bool))
print(a_int)
print(b_int)
print(type(a_int))
print(type(b_int))

a_list = [1,2,3,4,5]
print(a_list)
print(a_list[0])
print(a_list[1])

print(a_list[:2])
print(a_list[2:])

b_list = []
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)

c_list = [1, 3.14, "hello", [1,2,3]]
print(c_list)
print(c_list[1:3])

d_list = [1,2,3,4,5]
print(d_list)
d_list[0] = 5
print(d_list)

print("더하기:", 10+20)
print("빼기:", 10-20)
print("곱하기:", 10*20)
print("나누기:", 10/20)

print("c**2:", 10**2)
print("c**3:", 10**3)
print("c**4:", 10**4)

print("몫:", 40//6)
print("나머지:", 40%6)

print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)
print(False or False)
print(False or True)
print(True or False)
print(True or True)

print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)
print(False and False)
print(False and True)
print(True and False)
print(True and True)

print(not 0)
print(not 1)
print(not False)
print(not True)

print(10 == 10)
print(10 >= 10)
print(10 <= 10)
print(10 < 5)
print(10 > 5)
print(10 != 5)

a_list = ['a', 2, "hello", 3]
print('a' in a_list)
print( 1 in a_list)
print("hello" in a_list)
print(3 in in a_list)

a_str = "hello python"
print("python" in a_str)
print("py" in a_str)
print("40" in a_str)

a = 1
b = 1
if a == b :
    print("두 개의 값은 같습니다")
if a != b :
    print("두 개의 값은 같지 않습니다")

a = 1
b = 1
if a == b :
    print("a의 값이 더 크거나 같습니다")
if a != b :
    print("a의 값이 더 작거나 깉습니다")

a = 1
b = 1
c = 2
d = 4
if a == b and c == d :
    print("두 조건 모두 만족")
if a == b or c == db :
    print("두 조건 중 하나라도 만족")    

a_str = "hello python"
if a_str == "hello python"
    print("hello python 문자열이 같습니다.")
if a_str == "hi python"
    print("hello python 문자열이 같습니다.")
if "hello" in a_str == "hello python"
    print("hello 문자열이 포함되어 있습니다.")
if "hello" in not a_str == "hello python"
    print("hello 문자열이 포함되어 있지 않습니다.")    
if "hi" in nota_str == "hello python"
    print("hello python 문자열이 같습니다.")   

a_list = ["안녕", 1, 2, "파이썬"]
if "안녕" in a_list :
    print("a_list에 안녕 이 포함되어 있습니다")
if 2 in a_list :
    print("a_list에 숫자 2가 포함되어 있습니다")

a_list = ["안녕", 1, 2, "파이썬"]
if "안녕" not in a_list :
    print("a_list에 안녕 이 포함되어 있지 않습니다")
if 5 not in a_list :
    print("a_list에 숫자 5가 포함되어 있지 않습니다")

for i in range(7) :
    print(i)

for i in range(5, 10) :
    print(i)

for i in range(5, 10, -1) :
    print(i)   

a_list = [1,2,3,4,5, "안녕", "하세요"]
for i in a_list :
    print(i)

a_str = "hello python"
for i in a_str :
    print(i)

name_list = ["홍길동", "장다인", "김철수"]
age_list = [500, 5, 12]
for i,k in enumerate(name_list) :
    print("i=", i, end= '')
    print("k=", k)

name_list = ["홍길동", "장다인", "김철수"]
age_list = [500, 5, 12]
for i,k in enumerate(name_list) :
    print(k, end= '')
    print(age_list[i])
for i,k in enumerate(name_list) :
    print(name_list[i], end='')
    print(age_list[i])

name_list = ["홍길동", "장다인", "김철수"]
age_list = [500, 5, 12]
for i,k in range(len(name_list)) :
    print(name_list[i], end= '')
    print(age_list[i])

test_list = [i for i in range(10)]
print(test_list)

test2_list = []
for i in range(10) :
    test2_list.append(i)
print(test2_list)

test_list = [i * 5 i in range(10)]
print(test_list)
test2_list = [0 for i in range(10)]
print(test2_list)

a = 0
while a < 5 :
    print(a)
    a = a + 1

a = 0
while True :
    print(a)
    a = a + 1
    if a >= 5:
        break    