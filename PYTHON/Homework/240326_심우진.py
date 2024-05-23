3

print("%04d"%876)

print("%5s"%"CookBook")

print("%1.1f"%123.45)123.5

#  \n \b \\

4

2

== ,//,%,**

int,float,str

num =100 
num += 1
num -= 1
num *= 1
num /= 1
num= int(num)
print(num) 

num1,num2 = -100,100
print(num1 == num2)
print(num1>=num2)
print(num1<=num2)
print(num1!=num2)

num1,num2= -100,100
print((num1==num2)and (num1!=num2))
print((num1==num2) or (num1!=num2))
print((num1>=num2) and (num1<=num2))
print((num1>=num2) or (num1<=num2))
4

num = 0 
if num > 0:
    print("케이스1",end = ' ')
else:
    print("케이스2",end = ' ')
print("케이스3",end=' ')

num = int(input("정수를 입력하세요:"))
if num %5 != 0:
    print("5의 배수가 아닙니다.")
else: 
    print("5의 배수입니다.")

score = int(input("점수를 입력하세요:"))
if score >= 90:
    print("장학생",end=' ')
elif score >=60:
    print("합격",end= ' ')
else:
    print("불합격", end = ' ')
2

for i in range(0,101,1):
    print("여기를 반복")

for i in range(5,-1,-1):
    print("%d")

hap = 0 
for i in range(1,1001,5):
    hap += i #hap = hap + i
print(hap)

k = 0

for i in range(3333,10000,1):
    if i % 1234 != 0:
        continue
    
    k += i

    if k >= 1000000:
        k -= i
        break

print("값",k)

i = []  

for hap in range(3, 101):
    k = True
    
    for j in range(2, int(hap**0.5) + 1):
        if hap % j == 0:  
            k = False  
            break
    
    if k:  
        i.append(hap)  


for 소수 in i:
    print(소수, end = ' ')

year = 0 

if __name__ == "__main__": 
    year = int(input("연도를 입력하세요.:"))

    if ((year % 4 == 0))and (year % 100 !=0)or (year%400 == 0):
        print("%d년은 윤년입니다."%year)
    else:
        print("%d년은 윤년이 아닙니다."%year)

i,k,heartNum = 0,0,0
numStr,ch,heartStr = "","",""

if __name__ == "__main__" :
    numStr =input("숫자를 여러 개 입력하세요:")
    print("")
    i = 0
    ch = numStr[i]
    while True:
        heartNum = int(ch)

        heartStr =""
        for k in range(0,heartNum):
            heartStr +="\u2665"
            k += 1

        print(heartStr)

        i+=1
        if(i > len(numStr)- 1):
            break
        ch = numStr[i]


import random
nn=[]
for _ in range(10):
    num = random.randrange(1,100)
    nn.append(num)

hap = 0

for i in range(10):
    num = i             
    hap = hap +num
print(hap)

ary1= [1,2,3,4]
ary2=[]
for i in range(3,-1,-1):
    ary2.append(ary1[i])
print(ary1)
print(ary2)


append,extend,pop,index,count


myData = [[n*m for n in range (1,3)] for m in range(2,4)]
print(myData) > [[2, 4], [3, 6]]

1.리스트 2.딕셔너리 3.튜플 4.일반변수

append,remove,reverse,insert

myList = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print(myList[0][1]) 2
print(myList[1][3]) 8
print(myList[2]) [9, 10, 11, 12]

ss ='IT_CookBook'
print(ss[0]) > I

inStr = 'TI_CookBook_Python'
outStr= ''
for i in range(0,len(inStr)):
    if i%2 == 0:
        continue
    else:
        outStr += '#'
print("원본 내용-->",inStr)
print("변경 내용-->",outStr)

str1 ="코딩중에서 파이썬 코딩이 가장 즐거운 코딩"
print(str1.count('코딩'))
print(str1.rfind('코딩'))
print(str1.startswith('코딩'))
print(str1.find('코딩'))

3

21

True

0

text = "IT CookBook 데이터 분석을 365일 공부중임"

u = ""
l = ""
d = ""
h= ""
o= ""

for char in text:
    if char.isupper():
        u += char
    elif char.islower():
        l += char
    elif char.isdigit():
        d += char
    elif char.isalpha():
        h += char
    else:
        o+= char

print("대문자:", u)
print("소문자:", l)
print("숫자:", d)
print("한글:", h)
print("기타:", o)


def plus(v1,v2,v3):
    result = 0
    result =v1+v2+v3
    return result
hap = plus(100,200,300)
print(hap)















# def myFunc(p1=0,p2=0,p3=0):
#     ret= p1+p2+p3
#     return ret

# print("매개변수 없이 호출==>",myFunc())
# print("매개변수 1개 호출==>",myFunc(1))
# print("매개변수 2개 호출==>",myFunc(1,2))
# print("매개변수 3개 호출==>",myFunc(1,2,3))





# def func(v1,v2 =0 ,v3=0):
#     result = 0
#     result =v1+v2+v3
#     return result 4개다 작동은 됨
    

# import random

# data= []
# i,k =0,0

# if __name__ =="__main__":
#     for i in range(0,10):
#         tmp =hex(random.randrange(0,100000))
#         data.append(tmp)

#     print('정렬 전 데이터:',end ='')
#     [print(num,end=' ')for num in data]

#     for i in range(0,len(data)-1):
#         for k in range(i+1,len(data)):
#             if data[i],16)>int (data[k],16):
#                 tmp = data[k]
#                 data[i]=data[k]
#                 data= tmp

#     print('\n정렬 후 데이터:',둥 = '')
#     [print(num,emd= ''),for num in data]
            
# import random


# def getNumber(strData):
#     numStr =''
#     for ch in strData:
#         if ch.isdigit():
#         numStr+=ch


#     return int(numStr)


# data=[]
# i,k=0,0

#  if __name__ =="__main__":
#     for i in range(0,10):
#         tmp =hex(random.randrange(0,100000))
#         data.append(tmp)

#     print('정렬 전 데이터:',end ='')
#     [print(num,end=' ')for num in data]

#     for i in range(0,len(data)-1):
#         for k in range(i+1,len(data)):
#             if getNumber[i]>getNumber(data[k]):
#                 tmp = data[i]
#                 data[i]=data[k]
#                 data= tmp

#     print('\n정렬 후 데이터:',end = '')
#     [print(num,emd= ''),for num in data]