import streamlit as st
from bot_logic import answer_question

st.set_page_config(page_title="아진산업 분기보고서 챗봇", layout="wide")

st.title("📊 아진산업 분기보고서 챗봇")

st.write("분기보고서 내용이 궁금한 점을 아래에 입력해 주세요.")

user_input = st.text_area("질문을 입력하세요", height=100, placeholder="예) 2025년 3분기 매출 주요 변동 요인이 뭐야?")

if st.button("질문하기"):
    if user_input.strip():
        with st.spinner("분석 중입니다..."):
            answer = answer_question(user_input)
        st.markdown("### 🧾 답변")
        st.write(answer)
    else:
        st.warning("질문을 입력해 주세요.")
