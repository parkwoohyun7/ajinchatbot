import json

with open("data/ajin_data.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

def get_response(user_input):
    return knowledge_base.get(user_input, "죄송해요, 잘 모르겠어요. 다른 질문을 해주세요.")
