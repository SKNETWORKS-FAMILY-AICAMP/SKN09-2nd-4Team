import streamlit as st

def header():
    st.html('''<center>''')
    col1, col2, col3, col4, col5 = st.columns([5,3,3,3,5])
    # col2, col3, col4 = st.columns([3,3,3])
    with col2:
        st.page_link('main.py', label='HOME')
    with col3:
        st.page_link('pages/1_predict.py', label='PREDICT')
    with col4:
        st.page_link('pages/2_analysis.py', label='ANYLYZE')
    st.html('''</center>''')
        
def footer():
    st.html('''<center>develop with mvp copyright © 2025 YH, YJ, JY, YC</center>''')