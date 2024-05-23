# import random

# SIZE = 5
# pythonList = [ [random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE) ]

# for i in range(SIZE) :
#     for k in range(SIZE) :
#         print("%3d" % pythonList[i][k], end = ' ')
#     print()
# print()

# for i in range(SIZE) :
#     for k in range(SIZE) :
#         pythonList[i][k] += 100

# for i in range(SIZE) :
#     for k in range(SIZE) :
#         print("%3d" % pythonList[i][k], end = ' ')
#     print()
# print()


# import numpy as np

# SIZE = 5
# numpyAry = np.random.randint(0, 255, size = (SIZE, SIZE))

# print(numpyAry)
# print()

# numpyAry += 100

# print(numpyAry)




# import numpy as np
# import random

# numpyAry1 = [ random.randint(0,255) for _ in range(5)]
# print ('* array(pythonList)) --> ', numpyAry1)

# numpyAry2 = np.arange(5)
# print('* arange(5) --> ', numpyAry2)

# numpyAry3 = np.arange(3, 8)
# print('* arange(3, 8) --> ', numpyAry3)

# numpyAry3 = np.arange(0, 100, 20)
# print('* arange(0, 100, 20) --> ', numpyAry3)

# numpyAry4 = np.ones(5)
# print('* ones(5) --> \n', numpyAry4)

# numpyAry5 = np.ones((3,4))
# print('* ones((3,4)) --> \n', numpyAry5)

# numpyAry6 = np.zeros(5)
# print('* zeros(5) --> ', numpyAry6)

# numpyAry7 = np.empty(6)
# print('* empty(6) --> ', numpyAry7)

# numpyAry8 = np.full(5, 33)
# print('* full(5, 33) --> ', numpyAry8)

# numpyAry9 = np.identity(5)
# print('* identity(5) --> \n', numpyAry9)




# import random
# SIZE = 5
# startRow, startCol = 1, 1
# nSIZE = 3

# value = 1
# myList1 = []
# for _ in range(SIZE) :
#     tmpList = []
#     for _ in range(SIZE) :
#         tmpList.append(value)
#         value += 1
#     myList1.append(tmpList)

# for i in range(SIZE) :
#     [ print("%3d" % myList1[i][k], end= ' ') for k in range(SIZE) ]     
#     print()
# print()

# myList2 = []
# for i in range(startRow, startRow+nSIZE) :
#     tmpList = []
#     for k in range(startCol, startCol+nSIZE) :
#         tmpList.append(myList1[i][k])
#     myList2.append(tmpList)

# for i in range(nSIZE) :
#     [ print("%3d" % myList2[i][k], end= ' ') for k in range(nSIZE) ]  
#     print()
# print()     




# import numpy as np
# SIZE = 5

# imageAry = np.random.randint(0, 255, size=(SIZE, SIZE))
# print('### 1. 원본 ###')
# print(imageAry)
# np.save('source', imageAry)

# ##
# imageAry += 10
# print('### 2. 10 증가 ###')
# print(imageAry)
# np.save('result1', imageAry)

# ##
# imageAry = np.where( imageAry<128, 0, 255)
# print('### 3. 흑백 처리 ###')
# print(imageAry)
# np.save('result2', imageAry)

# ##
# imageAry = 255 - imageAry
# print(' ### 4. 반전 처리 ###')
# print(imageAry)
# np.save('result3', imageAry)

# ##
# imageAry = np.load('result2.npy')
# print('### 복구 1 :result2.npy ###')
# print(imageAry)

# ##
# imageAry = np.load('result1.npy')
# print('### 복구 2 :result1.npy ###')
# print(imageAry)

# ##
# imageAry = np.load('source.npy')
# print('### 복구 3(원본) : source.npy ###')
# print(imageAry)




# import matplotlib.pyplot as plt
# x_data = ['1st', '2nd', '3rd', '4th', '5th']
# y1_data = [90, 28, 75, 58, 78]
# y2_data = [80, 80, 50, 40, 90]
# y3_data = [40, 50, 90, 90, 60]
# plt.plot(x_data, y1_data, 'r-o', x_data, y2_data,'g:x', x_data, y3_data, 'b--p')
# plt.show()




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inFilename = "C:\\vscode\\source\\Excel\\singer.xlsx"
outFilename = "C:\\vscode\\source\\Excel\\singer_over6.xlsx"

df_senior = pd.read_excel(inFilename, 'senior', index_col= None)
df_junior = pd.read_excel(inFilename, 'junior', index_col= None)

df_singer = pd.concat( [df_senior, df_junior] ) 
df_singer_over6 = df_singer[df_singer['인원'] >= 6]
df_singer_over6 = df_singer_over6.sort_values(by = ['인원'], axis=0, ascending=False)
df_singer_over6 = df_singer_over6.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]

x_data = df_singer_over6['아이디']
y_data = df_singer_over6['유튜브 조회수']
colorAry = [ np.random.choice(['red', 'green', 'blue', 'brown', 'gold', 'lime', 'aqua', 'magenta', 'purple']) for _ in range(len(x_data))]

size = [10 * (y ** 0.5) for y in y_data]
x_data_sorted = sorted(x_data)

plt.scatter(x_data_sorted, y_data, color = colorAry, s=size)
plt.show()

# writer = pd.ExcelWriter(outFilename)
# df_singer_over6.to_excel(writer, sheet_name='singer', index=False)
# writer.save()
# print('SAVE.')



