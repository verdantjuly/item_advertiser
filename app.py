import streamlit as st

# streamlit document를 활용하여 예제가 아닌 나만의 것으로 만들어 보았다. 

st.title("동물 이미지 찾아 주기 🐯")
st.subheader("영어로 입력해 주세요.",divider="rainbow")
animal = st.chat_input("어떤 동물을 찾아드릴까요?")
if animal:
    with st.chat_message("ai"):
        st.text("잠시만 기다려 주세요.")
        st.image(f"https://edu.spartacodingclub.kr/random/?{animal}")
        st.text(f"예쁜{animal}가 나왔습니다.")
        
        