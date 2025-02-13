import os
import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
from header import header, footer
import random

# 페이지 설정
st.set_page_config(page_title="My App", page_icon="🚀", layout="centered", initial_sidebar_state="collapsed")

# 현재 파일의 경로
file_path = os.path.abspath(__file__)  # 현재 파일의 절대 경로
path = os.path.dirname(file_path)  # 디렉토리 경로
load_path = os.path.join(path, '../../data/Bank Customer Churn Prediction.csv')  # 데이터 파일 경로
df = pd.read_csv(load_path)
df_id_drop = df.drop('customer_id', axis=1)  # 불필요한 'customer_id' 컬럼 삭제

# 성별, 신용카드, 활성 회원 여부 변환 매핑
gender_map = {'남성': 'Male', '여성': 'Female'}
credit_card_map = {'존재': 1, '비존재': 0}
active_member_map = {'활성': 0, '비활성': 1}

header()

# 사이드바 필터링 옵션
st.sidebar.title("필터링")

# 나이
age_min = df['age'].min()
age_max = df['age'].max()
age_low, age_high = st.sidebar.slider('나이', min_value=0, max_value=100, value=(age_min, age_max), step=1)

# 신용점수
credit_score_min = df['credit_score'].min()
credit_score_max = df['credit_score'].max()
credit_score_low, credit_score_high = st.sidebar.slider('신용점수', min_value=0, max_value=1000, value=(credit_score_min, credit_score_max), step=50)

# 성별
gender_check = st.sidebar.segmented_control('성별', ['남성', '여성'], selection_mode="multi")
if gender_check:  # 성별 값이 선택되었을 때만 변환
    gender_check = [gender_map[g] for g in gender_check]

# 잔액
balance_min = int(df['balance'].min())
balance_max = int(df['balance'].max())
balance_low, balance_high = st.sidebar.slider('잔액', min_value=0, max_value=1000000, value=(balance_min, balance_max), step=1000)

# 상품 수
products_number_min = df['products_number'].min()
products_number_max = df['products_number'].max()
products_number_low, products_number_high = st.sidebar.slider('상품 수', min_value=1, max_value=4, value=(products_number_min, products_number_max))

# 가입 기간
tenure_min = df['tenure'].min()
tenure_max = df['tenure'].max()
tenure_low, tenure_high = st.sidebar.slider('가입 기간', min_value=0, max_value=50, value=(tenure_min, tenure_max))

# 활성 회원 여부
active_member_check = st.sidebar.segmented_control('활성 회원 여부', ['활성', '비활성'], selection_mode='multi')
if active_member_check:  # 활성 회원 값이 선택되었을 때만 변환
    active_member_check = [active_member_map[a] for a in active_member_check]

# 국가
country_check = st.sidebar.segmented_control('국가', ['France', 'Spain', 'Germany'], selection_mode='multi')

# 추정 급여
estimated_salary_min = int(df['estimated_salary'].min())
estimated_salary_max = int(df['estimated_salary'].max())
estimated_salary_low, estimated_salary_high = st.sidebar.slider('추정 급여', min_value=0, max_value=20000, value=(estimated_salary_min, estimated_salary_max), step=1000)

# 신용카드 여부
credit_card_check = st.sidebar.segmented_control('신용카드 여부', ['존재', '비존재'], selection_mode='multi')
if credit_card_check:  # 신용카드 여부 값이 선택되었을 때만 변환
    credit_card_check = [credit_card_map[c] for c in credit_card_check]

# 색상 팔레트 정의 (밝은 색상)
color_palette = ['#00BFFF', '#1E90FF', '#87CEFA', '#FFD700', '#FFA500', '#32CD32', '#FF69B4', '#8A2BE2', '#DC143C']

if st.sidebar.button('확인'):
    df_selection = df_id_drop[ 
        (df['age'] >= age_low) & (df['age'] < age_high) & 
        (df['credit_score'] >= credit_score_low) & (df['credit_score'] < credit_score_high) & 
        (df['gender'].isin(gender_check)) & 
        (df['balance'] >= balance_low) & (df['balance'] < balance_high) & 
        (df['products_number'] >= products_number_low) & (df['products_number'] < products_number_high) & 
        (df['tenure'] >= tenure_low) & (df['tenure'] < tenure_high) & 
        (df['active_member'].isin(active_member_check)) & 
        (df['country'].isin(country_check)) & 
        (df['estimated_salary'] >= estimated_salary_low) & (df['estimated_salary'] < estimated_salary_high) & 
        (df['credit_card'].isin(credit_card_check))
    ]

    # 1번째 행: 테이블
    st.subheader('필터링된 데이터')  # 제목 추가
    st.dataframe(df_selection)

    # 2번째 행: 나이별 이탈자 (차트)
    st.subheader('나이별 이탈자')  # 제목 추가
    age_chart = alt.Chart(df_selection).mark_bar().encode(
        x='age:O',
        y='count():Q',
        color=alt.Color('churn:N', scale=alt.Scale(range=random.sample(color_palette, len(df_selection['churn'].unique()))))
    )
    st.altair_chart(age_chart)

    # 3번째 행: 도넛 차트 (상품 수) 옆에 신용점수 vs 잔액 산점도 추가

    col3, col4 = st.columns([1, 1])  # 두 열로 분할
    with col3:
        st.subheader('상품 수별 고객 분포')  # 제목 추가
        donut = alt.Chart(df_selection).mark_arc(innerRadius=50).encode(
            theta="products_number",
            color=alt.Color('products_number:N', scale=alt.Scale(range=random.sample(color_palette, len(df_selection['products_number'].unique()))))
        )
        st.altair_chart(donut)
        
    with col4:
        st.subheader('신용점수 vs 잔액')  # 제목 추가
        churn_credit_score_chart = alt.Chart(df_selection).mark_point().encode(
            x='credit_score:Q',
            y='balance:Q',
            color=alt.Color('churn:N', scale=alt.Scale(range=random.sample(color_palette, len(df_selection['churn'].unique()))))
        )
        st.altair_chart(churn_credit_score_chart)

    # 4번째 행: 기간별 이탈자 차트 (산점도)

    col5, col6 = st.columns([3, 2])
    with col5:
        st.subheader('가입 기간별 이탈자')  # 제목 추가
        churn_tenure_chart = alt.Chart(df_selection).mark_line().encode(
            x='tenure:Q',
            y='count():Q',
            color=alt.Color('churn:N', scale=alt.Scale(range=random.sample(color_palette, len(df_selection['churn'].unique()))))
        )
        st.altair_chart(churn_tenure_chart)

    with col6:
        st.subheader('상품 수별 이탈자')  # 제목 추가
        churn_products_number_chart = alt.Chart(df_selection).mark_bar().encode(
            x='products_number:O',
            y='count():Q',
            color=alt.Color('churn:N', scale=alt.Scale(range=random.sample(color_palette, len(df_selection['churn'].unique()))))
        )
        st.altair_chart(churn_products_number_chart)

else:
    st.dataframe(df)
    st.write('세부 사항을 확인하기 위해선 좌측의 필터링을 적용하세요.')

footer()




