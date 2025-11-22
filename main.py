# main.py
from bot_logic import get_response

print("===== 아진산업 챗봇 =====")
print("종료하려면 'exit' 또는 '종료'라고 입력하세요.\n")

while True:
    user_input = input("사용자: ")
    if user_input.lower() in ["exit", "종료"]:
        print("챗봇 종료!")
        break
    response = get_response(user_input)
    print("챗봇:", response)
