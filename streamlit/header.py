import streamlit as st
import os

def header():
    file_path = os.path.abspath(__file__)
    path = os.path.dirname(file_path)
    _, col1, _ = st.columns([90,36,90])
    with col1:
        st.image(path + '/res/img/logo.png')
    st.html('''
    <style>
        header.stAppHeader {
            display: none;
        }
        .stMainBlockContainer {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        root, body {
            margin: 0;
            padding: 0;
        }
    ''')
    _, col2, col3, col4, _ = st.columns([40,25,27,30,30])
    with col2:
        st.page_link('main.py', label='HOME')
    with col3:
        st.page_link('pages/1_predict.py', label='PREDICT')
    with col4:
        st.page_link('pages/2_analysis.py', label='ANYLYZE')
        
def footer():
    file_path = os.path.abspath(__file__)
    path = os.path.dirname(file_path)

    _, coll, col, colr, _ = st.columns([5,7,2,6,5], vertical_alignment='center')
    with coll:
        st.html('''<center style="font-size:20px">developed by M.V.P</center>''')
    with col: 
        st.image(path + '/res/img/logo.png')
    with colr:
        st.html('''<center style="font-size:20px">copyright © 2025</center>''')