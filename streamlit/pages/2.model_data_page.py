import streamlit as st 

st.title('모델 정보 추가')

col1, col2 = st.columns(2)

with col1: 
    st.write('단독 모델')
with col2: 
    st.write(f"앙상블 모델")

