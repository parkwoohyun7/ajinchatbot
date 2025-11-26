from openai import OpenAI
from utils import load_report_text
import os
from dotenv import load_dotenv

# === 1. .env 파일에서 환경변수 로드 ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(ENV_PATH)  # .env 로드

# 디버그용: 실제로 키가 읽히는지 확인 (처음에만 보고, 나중에 지워도 됨)
print("DEBUG - OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# === 2. OpenAI 클라이언트 생성 ===
# 환경변수 OPENAI_API_KEY를 자동으로 사용
client = OpenAI()   # api_key를 여기서 안 넘겨도 .env에서 읽어옴

# === 3. 앱 시작할 때 한 번만 분기보고서 텍스트 로딩 ===
REPORT_TEXT = load_report_text()


def answer_question(user_input: str) -> str:
    """
    사용자 질문(user_input)을 받아서
    분기보고서 내용을 참고해 답변을 생성
    """
    # 분기보고서를 못 읽었을 때 처리
    if not REPORT_TEXT:
        return "분기보고서 파일을 읽지 못했습니다. data/분기보고서.txt를 확인해주세요."

    # 시스템 프롬프트: 챗봇의 역할/말투 정의
    system_prompt = """
너는 아진산업의 '분기보고서'를 기반으로 답변하는 회사 챗봇이다.
- 분기보고서 내용에 근거해서 답변한다.
- 너는 총무인사팀에 직원관점으로 말한다.
- 한국어로 정중하게, 하지만 너무 딱딱하지 않게 답변한다.
"""

    # 유저 프롬프트: 보고서 내용 + 사용자 질문 같이 전달
    user_prompt = f"""
[분기보고서 내용]
{REPORT_TEXT}

[사용자 질문]
{user_input}

위 분기보고서 내용만 참고해서 답변해줘.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # 사용하려는 모델 이름
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            # 필요하면 옵션 추가 가능
            # max_tokens=800,
            # temperature=0.2,
        )

        return response.choices[0].message.content

    except Exception as e:
        # ✅ API 호출 중 에러가 발생했을 때 상세 내용 보여주기
        import traceback
        print("===== OpenAI API 오류 발생 =====")
        print(e)
        traceback.print_exc()
        print("================================")

        # 화면에도 에러 내용 그대로 보여주기
        return f"오류가 발생했습니다: {type(e).__name__}: {e}"
