from openai import OpenAI
from utils import load_report_text
import os

# OPENAI_API_KEY는 환경변수에서 읽음
client = OpenAI()

# 앱 시작할 때 한번만 보고서 읽기
REPORT_TEXT = load_report_text()

def answer_question(user_input: str) -> str:
    """
    사용자 질문(user_input)을 받아서
    분기보고서 내용을 참고해 답변을 생성
    """
    if not REPORT_TEXT or "찾을 수 없습니다" in REPORT_TEXT:
        return "분기보고서 파일을 읽지 못했습니다. data/분기보고서.txt를 확인해주세요."

    system_prompt = """
너는 아진산업의 '분기보고서'를 기반으로 답변하는 회사 내부용 챗봇이다.
- 반드시 분기보고서 내용에 근거해서만 답변한다.
- 모르는 내용은 아는 척하지 말고 '분기보고서에 없는 내용입니다'라고 답한다.
- 한국어로 정중하게, 하지만 너무 딱딱하지 않게 답변한다.
"""

    user_prompt = f"""
[분기보고서 내용]
{REPORT_TEXT}

[사용자 질문]
{user_input}

위 분기보고서 내용만 참고해서 답변해줘.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # 사용하려는 모델 이름
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content
