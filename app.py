import streamlit as st
from bot_logic import get_response

st.title("아진산업 챗봇")
st.write("궁금한 사항을 입력하면 챗봇이 답변합니다!")

user_input = st.text_input("질문을 입력하세요:")
if user_input:
    response = get_response(user_input)
    st.write("챗봇:", response)
