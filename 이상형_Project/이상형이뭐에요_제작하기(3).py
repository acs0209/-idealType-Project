# 답변은 total_dictionary을 한바퀴 싹돌면서 질문을보고 그 질문에 따라서 하나씩 달아준다


total_dictionary = {}
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

# 지금 i에는 total_dictionary의 key들이 들어간다 그래서 입력받은 answer가 total_dictionary의 
# value로 들어간다 total_dictionary[i] = answer을 통해서
for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)