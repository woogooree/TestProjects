# sorted key 속성 lambda 기억 안나서 그것만 검색했음

student = [['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]
print("정렬 전 -->", student)

sortStudent = sorted(student, key= lambda student: (student[1]))
print("정렬 후 -->", sortStudent)

print("## 성적별 조 편성표 ##")
for i in range(0, 3) :
    a = student.pop()[0]
    b = sortStudent.pop()[0]

    print(a, " : ", b)

