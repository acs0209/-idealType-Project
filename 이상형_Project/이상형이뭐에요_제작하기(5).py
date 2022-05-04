total_list = []

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

# total_list에 딕셔너리자체가 저장이 되어있다 따라서 i에는 딕셔너리 하나하나가 들어가게 된다
# 그럼 이제 그 딕셔너리중에서 질문만 꺼내고 싶으니까 print(i["질문"])이라고 작성한다
# 그러면 그 질문에 맞는 답변을 작성할껀데 i["답변"] = answer을 통해 딕셔너리에 답변 : answer라는 새로운 키:값 형태를 추가한다
for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)