import streamlit as st
from ai_image import ai_image 
from ai_text import ai_text

st.title("제품 홍보 포스터 생성기")
st.subheader("당신의 제품을 홍보하고 포스터로 만들어드립니다.",divider="rainbow")
item = st.chat_input("어떤 제품을 홍보해 드릴까요?")
if item:
    with st.spinner("생성 중입니다"):
        image = ai_image(item)
        text = ai_text(item)
        with st.chat_message("ai"):
            st.image(image)
            st.text(text)

    

        
        