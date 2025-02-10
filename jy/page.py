# streamlit page 생성
# streamlit run jy/page.py

import streamlit as st
from catboost import CatBoostClassifier

def main():
    st.title("고객 이탈 예측")
    st.write('CatBoost 모델을 사용한 고객 이탈 예측입니다.')
    cat = CatBoostClassifier()
    cat.load_model('./model/catboost_model.cbm')
    # ['credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card', 'active_member', 'estimated_salary', 'country']
    # 위 데이터들을 입력 받기
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        credit_score = st.number_input('신용점수', min_value=300, max_value=850)
        age = st.number_input('나이', min_value=18, max_value=100)
        estimated_salary = st.number_input('추정 급여', min_value=0)
    with col2:
        balance = st.number_input('잔액', min_value=0)
        products_number = st.number_input('상품 수', min_value=1, max_value=4)
        tenure = st.number_input('가입기간', min_value=0, max_value=20)
    with col3:
        country = st.selectbox('국가', ['France', 'Spain', 'Germany'])
        credit_card = st.checkbox('신용카드 여부')
        active_member = st.checkbox('활성 회원 여부')
    input_data = [[credit_score, age, tenure, balance, products_number, credit_card, active_member, estimated_salary, country]]
    # st.write(input_data)
    
    # session_state 초기화
    if "pred_proba" not in st.session_state:
        st.session_state.pred_proba = []
    with col3:
        # 빈 박스
        st.header(' ')
        # 버튼 클릭 시 새로운 예측 실행
        if st.button('확인'):
            st.session_state.pred_proba.append(cat.predict_proba(input_data)[0][1])
            

    # 예측 결과 표시
    if st.session_state.pred_proba is not None:
        st.write('고객 이탈 확률은 다음과 같습니다.')
        for i, pred in enumerate(st.session_state.pred_proba):
            st.write(f"예측 결과: {pred:.5f}")

if __name__ == '__main__':
    main()