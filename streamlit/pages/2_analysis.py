import os
import numpy as np 
import pandas as pd 
import streamlit as st 
import altair as alt 

# 현재 파일의 경로
file_path = os.path.abspath(__file__) # 정규화된 절대화된 버전 반환, __file__ : 경로, 이 파일의 경로를 말하는 듯 
path = os.path.dirname(file_path) # 경로의 디렉토리 이름을 반환 (이 파일의 이름을 제외한 디렉토리 경로 반환-> 이를 통해 현재 파일이 위치한 폴더 경로를 쉽게 추출할 수 있음)

st.title("고객 이탈 예측")
st.write('앙상블(스태킹) 모델을 사용한 고객 이탈 예측입니다.')
load_path = os.path.join(path, '../../data/Bank Customer Churn Prediction.csv') # 어떤 위치에 접근하고 싶은지 명시, join 으로 여로 경로를 결합

df = pd.read_csv(load_path)
# customer_id,credit_score,country,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,churn

df_id_drop = df.drop('customer_id', axis=1)
df_numitic = df.select_dtypes('number')
# df_str = df.select_dtypes('str')

st.dataframe(df_id_drop, use_container_width=True)

st.area_chart(data=df_numitic, x = 'churn', y = ['tenure', 'products_number'],use_container_width=True) #, *, x=없음, y=없음, x_라벨=없음, y_라벨=없음, 색상=없음, 스택=없음, 너비=없음, 높이=없음, use_container_width=True)

st.bar_chart(data=df_id_drop, x='churn', y=['tenure', 'products_number'], horizontal=False, stack=False, use_container_width=True)

st.line_chart(data=df_numitic, x='churn', y=['tenure', 'products_number'], use_container_width=True)

# 얼만틈의 비용을 줄일 수 있는지 계산

st.scatter_chart(data=df_numitic, x='churn', y=['tenure', 'products_number'], x_label=None, y_label=None, color=None, size=None, width=None, height=None, use_container_width=True)

donut = alt.Chart(df_numitic).mark_arc(innerRadius=50).encode(
    theta="products_number",
)

st.altair_chart(donut)