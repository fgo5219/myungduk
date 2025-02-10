import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# 페이지 기본 설정
st.set_page_config(
    page_title="6하원칙 기반 작문 도우미",
    page_icon="📝",
    layout="wide"
)

# 제목 표시
st.title("6하원칙 기반 작문 도우미 🤖")
st.markdown("---")

#Gemini API 키 설정
api_key = st.text_input("Gemini API 키를 입력하세요:", type="password")


# Gemini Pro 모델 초기화
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0.7, api_key=api_key)

# 사용자 입력 받기
who = st.text_input("누가?", placeholder="주체를 입력하세요")
when = st.text_input("언제?", placeholder="시간을 입력하세요")
where = st.text_input("어디서?", placeholder="장소를 입력하세요")
what = st.text_input("무엇을?", placeholder="행위/사건을 입력하세요")
why = st.text_input("왜?", placeholder="이유를 입력하세요")
how = st.text_input("어떻게?", placeholder="방법을 입력하세요")

if st.button("글 작성하기"):
    if who and what and when and where and why and how:
        # 프롬프트 구성
        prompt = f"""
        다음 정보를 바탕으로 자연스러운 글을 작성해주세요:
        - 누가: {who}        
        - 언제: {when}
        - 어디서: {where}        
        - 무엇을: {what}
        - 왜: {why}
        - 어떻게: {how}
        
        다음 조건을 반드시 지켜주세요:
        1. 모든 6하원칙 요소를 자연스럽게 포함할 것
        2. 문장을 자연스럽게 연결할 것
        3. 한국어로 작성할 것
        4. 3문단 이하로 구성할 것
        """
        
        # AI 응답 생성
        response = llm.invoke(prompt)
        
        # 결과 표시
        st.markdown("### 작성된 글:")
        st.write(response.content)
        
    else:
        st.warning("모든 항목을 입력해주세요!")

# 페이지 하단 정보
st.markdown("---")
st.markdown("Made with ❤️ by Jeong Swug Hyeon")
