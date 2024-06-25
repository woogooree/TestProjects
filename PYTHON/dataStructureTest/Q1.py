text = "진달래꽃", "나 보기가 역겨워", "가실 때에는", "말없이 고이 보내드리오리다."

print("----- 원본 -----")
for i in range(0, 4) :
    print(text[i])

print("----- 거꾸로 처리된 결과 -----")
for i in range(3, -1, -1) :
    textList = list(text[i])
    textList.reverse()
    revText = ''.join(textList)
    print(revText)

    # 내가 이겼다