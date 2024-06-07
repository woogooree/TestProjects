save = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]

add = input("추가할 친구 --> ")
times = int(input("카톡 횟수 --> "))

save.append((add, times))
save = sorted(save, key=lambda x : (x[1]), reverse=True)

print(save)