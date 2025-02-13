# streamlit page 생성
# streamlit run jy/page.py
import os
import streamlit as st
from joblib import load
from header import header, footer
import random

# 현재 파일의 경로
file_path = os.path.abspath(__file__)
path = os.path.dirname(file_path)

st.set_page_config(page_title="My App", page_icon="🚀", layout="centered", initial_sidebar_state="collapsed")

header()

st.title("고객 이탈 예측")
st.write('앙상블(스태킹) 모델을 사용한 고객 이탈 예측입니다.')
load_path = os.path.join(path, '../../model/stacking.joblib')
model = load(load_path)
# ['credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'country']
# 위 데이터들을 입력 받기

col1, col2, col3 = st.columns(3)

with col1:
    # age = st.number_input('나이', min_value=18, max_value=100)
    # age = st.selectbox('나이', range(10, 80, 10))
    # age = st.slider('나이', min_value=18, max_value=100, value=30)
    ages = ['청년', '중년', '장년', '노년']
    age = ages.index(st.selectbox('나이', ages))
    age = [29, 50, 70, 90][age]
    # credit_score = st.number_input('신용점수', min_value=300, max_value=850)
    credit_score = st.slider('신용점수', min_value=300, max_value=850, value=500)
    # estimated_salary = st.number_input('추정 급여', min_value=0)
    gender = st.segmented_control('성별', ['남성', '여성'], default='남성')
    gender = ['남성', '여성'].index(gender)


with col2:
    # balance = st.number_input('잔액', min_value=0)
    balance = st.slider('잔액', min_value=0, max_value=250000, value=100000)
    # products_number = st.number_input('상품 수', min_value=1, max_value=4)
    products_number = st.slider('상품 수', min_value=1, max_value=4, value=2)
    # tenure = st.number_input('가입기간', min_value=0, max_value=20)
    active_member = st.checkbox('활성 회원 여부')

with col3:
    # country = st.selectbox('국가', ['France', 'Spain', 'Germany'])
    # country = ['France', 'Spain', 'Germany'].index(country)
    tenure = st.slider('가입기간', min_value=0, max_value=20, value=10)
    estimated_salary = st.slider(
        '추정 급여', min_value=0, max_value=200000, value=100000)
    credit_card = st.checkbox('신용카드 여부')
    # [credit_score	country	gender	age	tenure	balance	products_number	credit_card	active_member	estimated_salary	]
input_data = [[credit_score, random.randint(0, 2) , gender, age, tenure, balance, products_number,
                credit_card, active_member, estimated_salary]]

# session_state 초기화
if "pred_proba" not in st.session_state:
    st.session_state.pred_proba = []
with col3:
    # 빈 박스
    st.header(' ')
    # 버튼 클릭 시 새로운 예측 실행
    if st.button('확인'):
        st.session_state.pred_proba = [model.predict_proba(
            input_data)[0][1]] + st.session_state.pred_proba

# 예측 결과 표시
if st.session_state.pred_proba is not None:
    st.write('고객 이탈 확률은 다음과 같습니다.')
    for i, pred in enumerate(st.session_state.pred_proba):
        st.write(f"예측 결과: {pred:.5f}")

footer()