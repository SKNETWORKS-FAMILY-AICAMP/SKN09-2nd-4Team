import streamlit as st

def header():
    st.html('''<center>''')
    col1, col2, col3, col4, col5 = st.columns([5,3,3,3,5])
    with col2:
        st.page_link('main.py', label='HOME')
    with col3:
        st.page_link('pages/1_predict.py', label='PREDICT')
    with col4:
        st.page_link('pages/2_analysis.py', label='ANALYZE')
    st.html('''</center>''')
        
def footer():
    st.html('''<center>develop with mvp copyright © 2025</center>''')