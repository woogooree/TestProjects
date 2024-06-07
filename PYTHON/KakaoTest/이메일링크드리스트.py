from Slist import SList

while True :
    
    name = input("이름 --> ")
    if name == '':
        break

    elif __name__ == '__main__' :
        email = input("이메일 --> ")

        s = SList()
        s.insert_front((name, email))
        
s.print_list()
print("사용종료")
