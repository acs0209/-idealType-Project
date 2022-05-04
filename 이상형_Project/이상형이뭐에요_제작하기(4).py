total_list = []

# total_list라는 리스트에 우리는 아래 딕셔너리를 추가할꺼다 질문을 입력받고 question라는 변수에 넣은 후
# else경우에 딕셔너리가 만들어 져서 total_list에 추가가 된다.
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})
