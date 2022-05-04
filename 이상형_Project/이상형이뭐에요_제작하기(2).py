# 딕셔너리를 만들고 while문을 돌면서 입력(질문)을 받을꺼다 입력 받은 질문을 question라는 변수에 넣는다
# 그리고 만약에 question이 q라면 break가되서 while문이 종료되고 아니면 total_dictionary[question]에
# "" 을 넣는다 지금은 딕셔너리 key만 만들고 있으니 total_dictionary[question] = ""이런 형태로 보관하고 있다

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""
print(total_dictionary)