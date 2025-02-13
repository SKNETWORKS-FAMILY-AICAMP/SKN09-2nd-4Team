import streamlit as st

def header():
    col1, col2, col3, col4, col5 = st.columns([5,3,3,3,5])
    with col2:
        st.page_link('main.py', label='HOME')
    with col3:
        st.page_link('pages/1_predict.py', label='PREDICT')
    with col4:
        st.page_link('pages/2_analyze.py', label='ANYLYZE')