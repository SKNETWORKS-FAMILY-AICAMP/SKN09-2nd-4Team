import streamlit as st 
import os
from header import header, footer

st.set_page_config(page_title="My App", page_icon="🚀", layout="centered", initial_sidebar_state="collapsed")

file_path = os.path.abspath(__file__)
path = os.path.dirname(file_path)
    
header()

st.html('''
<style>
    root, body {
        margin: 0;
        padding: 0;
    }
    nav {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    a {
        margin: 0 10px;
        text-decoration: none;
    }
    a:hover {
        color: blue;
    }
    img {
        border-radius: 10px;
    }
    img:hover{
        transform:scale(1.025);
        transition: transform .5s;        
    }
</style>

<center style="padding:10px;border-radius:10px;">
    <header>develop with mvp</header>
    <h1>은행 고객 이탈 분석 및 예측</h1>
    <p>방대한 데이터를 통해 고객들을 분석하고 최신 AI 모델을 이용하여 고객 이탈을 예측하고 인사이트를 얻어 보세요</p>
</center>
''')

st.image(path+"/res/img/chart1.png", use_container_width=True)

st.html('''
<div style="padding:10px;border-radius:10px; text-align:center;">
    <h1>높은 가격 효용성</h1>
    <p>합리적인 비용으로 고객 이탈을 예측하고 최적의 전략을 수립하여 보다 나은 서비스를 제공합니다.</p>
<div>
''')

st.image(path+"/res/img/chart2.webp", use_container_width=True)

st.html('''
<div style="padding:10px;border-radius:10px; text-align:center;">
    <h1>다양한 시각화 지표</h1>
    <p>고객 이탈을 예측하기 위한 다양한 시각화 지표를 제공하여 인사이트 도출에 도움을 줍니다.</p>
<div>
''')

st.image(path+"/res/img/chart3.png", use_container_width=True)

st.html('''
<div style="padding:10px;border-radius:10px; text-align:center;">
    <h1>머신러닝 최적화</h1>
    <p>다양한 머신러닝 모델을 사용하여 고객 이탈을 예측하고 최적의 모델을 사용함으로써 정확도를 높입니다.</p>
<div>
''')

st.image(path+"/res/img/chart4.webp", use_container_width=True)

st.html('''
<div style="padding:10px;border-radius:10px; text-align:center;">
    <h1>고객 트렌드 분석</h1>
    <p>고객들의 트렌드를 분석하여 고객 이탈을 예측하고 최적의 전략을 수립하여 마케팅 비용 손실을 최소화합니다.</p>
<div>
''')

st.image(path+"/res/img/chart5.webp", use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image(path+"/res/img/chart4.webp", use_container_width=True)
    st.write('고객 이탈 예측을 위한 다양한 시각화 지표')
with col2:
    st.image(path+"/res/img/chart5.webp", use_container_width=True)
    st.write('고객 이탈 예측을 위한 다양한 시각화 지표')
with col3:
    st.image(path+"/res/img/chart5.webp", use_container_width=True)
    st.write('고객 이탈 예측을 위한 다양한 시각화 지표')

footer()