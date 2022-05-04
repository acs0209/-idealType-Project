# 아래 두 방법은 데이터를 저장하는 방식이 다를뿐이다
# 첫번째 방법은 딕셔너리를 만들어서 key:value형태로 데이터를 저장하는거다
# 두번째 방법은 리스트에 딕셔너리를 만들어서 딕셔너리 자체를 리스트에 저장하는거다


# 첫번째 방법
total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)


# 두번째 방법
total_list = []
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})


for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)

