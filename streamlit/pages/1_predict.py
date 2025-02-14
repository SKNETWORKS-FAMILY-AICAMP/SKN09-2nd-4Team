# streamlit page 생성
# streamlit run jy/page.py
import os
import streamlit as st
from joblib import load
from header import header, footer

# 현재 파일의 경로
file_path = os.path.abspath(__file__)
path = os.path.dirname(file_path)

st.set_page_config(page_title="My App", page_icon="🚀", layout="centered", initial_sidebar_state="collapsed")

header()

st.html('''
    <div style="padding:10px;border-radius:10px; text-align:center;">
        <h1>고객 이탈 예측</h1>
        <p>앙상블(스태킹) 모델을 사용한 고객 이탈 예측입니다.</p>
    </div>
''')

load_path = os.path.join(path, '../../model/stacking.joblib')
model = load(load_path)

col1, col2, col3 = st.columns([2,2,3])

with col1:
    country = st.selectbox('국가', ['France', 'Germany', 'Spain'])
    country = ['France', 'Germany', 'Spain'].index(country)
    balance = st.slider('잔액', min_value=0, max_value=250000, value=100000)
    estimated_salary = st.slider('추정 급여', min_value=0, max_value=200000, value=100000)


with col2:
    ages = ['청년', '중년', '장년', '노년']
    age = ages.index(st.selectbox('나이', ages))
    age = [29, 50, 70, 90][age]
    products_number = st.slider('상품 수', min_value=1, max_value=4, value=2)
    tenure = st.slider('가입기간', min_value=0, max_value=20, value=10)

with col3:
    gender = st.segmented_control('성별', ['남성', '여성'], default='남성')
    gender = ['남성', '여성'].index(gender)
    credit_score = st.slider('신용점수', min_value=300, max_value=850, value=500)
    col31, col32 = st.columns(2)
    with col31: 
        active_member = st.checkbox('활성 회원 여부')
    with col32:
        credit_card = st.checkbox('신용카드 여부')
    
input_data = [[credit_score, country, gender, age, tenure, balance, products_number,
                credit_card, active_member, estimated_salary]]

# session_state 초기화
if "pred_proba" not in st.session_state:
    st.session_state.pred_proba = 0.0
with col3:
    # 버튼 클릭 시 새로운 예측 실행
    col31, col32, _ = st.columns([2,2,1])
    
    with col31:
        if st.button('확인'):
            st.session_state.pred_proba = model.predict_proba(input_data)[0][1]
    with col32:
        if st.button('초기화'):
            st.session_state.pred_proba = 0.0

# 예측 결과 표시
if st.session_state.pred_proba is not None or st.session_state.pred_proba != 0.0:
    st.write('고객 이탈 예측 확률은 다음과 같습니다.')
    st.write(f"예측 결과: {st.session_state.pred_proba:.4f}")

footer()