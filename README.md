# SKN09-2nd-4Team

# 0. Team Introduction (팀 소개)

### 👑팀명: MVP ("Million Vault Protector") 

![Image](https://github.com/user-attachments/assets/92e589e1-f3ea-447d-94a4-3aeb6625956a)

- 프로젝트 기간: 2025.02.03 ~ 2025.02.14
<table align=center>
  <tbody>
    <tr>
    <br>
      <td align=center><b>박유진</b></td>
      <td align=center><b>서예찬</b></td>
      <td align=center><b>조이현</b></td>
      <td align=center><b>허정윤</b></td>
    </tr>
    <tr>
      <td align="center">
          <img alt="Image" src="https://github.com/user-attachments/assets/1d433d60-8af5-4619-82a6-01d176bc2b00" width="200px;" alt="박유진"/>
      <td align="center">
          <img alt="Image" src="https://github.com/user-attachments/assets/a56c575d-c9e4-4c86-b7d5-4d8d9bd98127" width="200px;" alt="서예찬"/>
      </td>
      <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/60cacd87-c100-4e8e-ba64-cd68acc4aa97" width="200px;"alt="조이현" />
      </td>
      <td align="center">
        <img alt="Image" src="https://github.com/user-attachments/assets/fe203939-74eb-41e5-be0b-c41f53477ee8" width="200px;" alt="허정윤"/>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/YUJINDL01"><div align=center>@YUJINDL01</div></a></td>
      <td><a href="https://github.com/syc9811"><div align=center>@syc9811</div></a></td>
      <td><a href="https://github.com/SIQRIT"><div align=center>@SIQRIT</div></a></td>
      <td><a href="https://github.com/devunis"><div align=center>@devunis</div></a></td>
    </tr>
  </tbody>
</table>
<br>
<br>
<br>

# 1. Project Introduction (프로젝트 개요)

### 프로젝트 명

- **👑MVP👑**: 데이터 기반 ABC 은행 가입고객 이탈자 분석 및 예측

### 프로젝트 소개
- 본 프로젝트는 데이터 분석 및 머신러닝을 활용하여 ABC 은행 고객의 이탈 가능성을 예측하는 모델을 개발하는 것을 목표로 합니다. 이를 통해 ABC 은행은 고객 이탈을 사전에 감지하고, 
맞춤형 마케팅 전략을 수립하여 고객 유지율을 높일 수 있을 것입니다.

### 프로젝트 배경

![image](https://github.com/user-attachments/assets/cb482edb-53a0-40a9-a7d1-17ef4e1a8a18)

- 현대 금융 시장에서 고객 유지는 은행 및 금융 기관의 지속 가능한 성장을 위해 필수적인 요소입니다. 그러나, 현대의 전통적인 은행의 마케팅 비용은 증가한 반면, 고객이 이탈하는 상황에 직면했습니다. 또한 시중 은행에 대한 고객 충성도도 하락하는 경향을 보입니다.

![image](https://github.com/user-attachments/assets/3a3ecd71-6f16-42f6-b811-c7069a9588a7)

- Harvard Business Review Reprint-"The Economics of E-Loyalty" (2002) by Frederick F. Reichheld & Phil Schefte-에 따르면, 기존 고객을 유지하는 비용은 신규 고객을 유치하는 비용보다 5배 저렴하다고 알려져 있습니다. 따라서, 기존 고객의 이탈을 방지하는 것이 운영 비용 절감 및 수익성 강화에 효과적인 전략이 될 수 있습니다.

  ![image](https://github.com/user-attachments/assets/fd4d2a7e-0580-43ca-9aed-375a82904b1f)

- 하지만 Sage Journal-Reducing Adverse Selection through Customer Relationship Management
Yong Cao and Thomas S. Gruca-에 따르면, 많은 금융 기관은 고객 이탈이 발생한 후에 대응하는 사후 관리 방식에 의존하고 있어 실질적인 비용 절감과 고객 유지 효과를 극대화하는 데 어려움을 겪고 있습니다. 이에 따라, 사전적으로 고객 이탈을 예측하고 선제적으로 대응할 수 있는 데이터 기반의 고객 이탈 예측 모델이 필요하게 되었습니다.
<br>

#### 데이터 및 접근 방법
- 데이터 수집: 고객의 거래 내역, 계좌 유형, 대출 이력, 고객 서비스 이용 패턴 등 ABC 은행의 데이터셋을 활용.
- 데이터 전처리 및 시각화: 결측치 및 이상치 확인, 데이터 정규화 등의 과정을 수행.
- 특성 엔지니어링: 고객 연령, 소득 수준, 신용 점수, 계좌 잔액 변화, 대출 상환 이력 등의 중요한 특성 추출
- 모델 사용: XGBoost, RandomForest, CatBoost, AdaBoost 등 다양한 머신러닝 알고리듬을 적용하여 예측 성능 비교 분석
- 모델 평가: 상위 4개 모델에 대한 앙상블을 적용하여 정확도, 정밀도, 재현율, F1-score 및 ROC-AUC 등의 성능 지표를 활용한 모델 최적화 및 평가
<br>

#### 기대 효과
- 고객 이탈 사전 예방: 이탈 가능성이 높은 고객을 조기에 발견하여 맞춤형 프로모션 및 상담 제공
- 비용 절감: 고객 유지 비용 절감 및 신규 고객 유치 비용 최소화
- 비즈니스 성장: 데이터 기반 의사결정을 통한 은행의 경쟁력 강화 및 고객 만족도 향상
<br>

#### 결론
본 프로젝트를 통해 은행은 고객 이탈 문제를 보다 효과적으로 해결하고, 장기적인 고객 관계 관리를 강화할 수 있습니다. 데이터 기반의 예측 모델을 활용하여 고객 맞춤형 전략을 수립함으로써 은행의 지속 가능한 성장을 도모하는 것이 본 프로젝트의 최종 목표입니다.
<br>
<br>
<br>

# 2. 기술 스택

###  협업 및 문서화  
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=Discord&logoColor=white)   

###  도구  
![VSCode](https://img.shields.io/badge/VScode-007ACC?style=for-the-badge&logo=Visual-Studio-Code&logoColor=white)

###  형상 관리
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) 
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)  

###  프로그래밍 언어  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)  

###  데이터 분석  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white) 
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white)  

###  머신러닝  
![Scikit-Learn](https://img.shields.io/badge/Scikit%20Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)  

###  데이터 시각화  
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=Matplotlib&logoColor=white) 
![Seaborn](https://img.shields.io/badge/Seaborn-4C8CBF?style=for-the-badge&logo=Seaborn&logoColor=white)  

### 🔗 대시보드  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)  
<br>
<br>
<br>

----

# 3. WBS

# 4. 데이터 전처리 결과서 (EDA)

### 데이터 수집 및 선정
> https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset


### 데이터 전처리 
>
> **1) 데이터 내용 확인**
>
>
>![Image](https://github.com/user-attachments/assets/5320d17c-6150-4db4-9222-68cb717fba02)
>
>
>
>
>포함된 주요 변수 : credit_score (신용 점수), country (국가), age (나이), tenure (가입 기간),churn (이탈 여부)등의 주요 변수
>
>데이터 크기 : 총 10000명의 고객 데이터, 12개의 변수 (2개의 object형 변수, 8개의 int형 변수, 2개의 float형 변수)
>
> **2) 결측치 확인**
>
>
>
>
>![Image](https://github.com/user-attachments/assets/51f85bf6-2824-4b7b-a28c-434d9914b3a7)
>
>
>
>
>
>
>결측치 확인결과 결측치없음
>
>
>**3) 이상치 확인**
>
>
>
>
>![Image](https://github.com/user-attachments/assets/dd1cd53f-0987-47e0-883c-1e69532c10c3)
>
>이상치 확인 결과, age(나이) 컬럼에서 이상치가 발견되었지만, 검토한 결과 고령 고객들의 나이가 높은 것으로 확인되었음. 따라서 별도의 조치는 취하지 않았음.
>
>
>**4)데이터 시각화(임시)**
>
>
>![Image](https://github.com/user-attachments/assets/50010858-bfdc-462e-adaf-91d9d99ef55c)
>
>
>![Image](https://github.com/user-attachments/assets/800c94ce-3527-444b-83ef-a9796548e74d)
>
>![Image](https://github.com/user-attachments/assets/453e84ed-d593-43a3-82ff-45d20984d04d)
>
>![Image](https://github.com/user-attachments/assets/452e73bb-9e95-4cff-a2fa-536a8fc3a1b8)
>
>![Image](https://github.com/user-attachments/assets/7d11f50c-7e7a-42a5-bdb2-660dccc7dbce)
>
>
>![Image](https://github.com/user-attachments/assets/9851172e-cd92-4835-8348-d3cfb9478a32)
























----

# 5. 인공지능 학습 결과서
- 왜 머신러닝인가
- 왜 해당 모델인가
- 학습된 인공지능 모델

# 6. 수행결과(테스트 결과 화면 또는 시연 페이지)

# 7. 한 줄 회고
- 박유진:
- 서예찬:
- 조이현: EDA 과정에서 범주형 데이터 컬럼별 데이터프레임에 대한 상관계수 편차가 큰 것을 확인했다. 따라서, 각각의 최적화된 머신러닝을 튜닝하는 것까지 시도해보고 싶었지만, 시간적 여건이 되지 않아 아쉬울 따름이다.
- 허정윤: 

## README.md 작성 내용


---
**SK네트웍스 Family AI 캠프 9기 2차 프로젝트**

1. 팀 소개(완)

- 팀명(완)
- 멤버 개인 깃허브 계정과 연동(완)

2. 프로젝트 개요(완)

- 프로젝트 명(완)
- 프로젝트 소개(완)
- 프로젝트 필요성(배경)(완)
- 프로젝트 목표(완)

3. 기술 스택(완)

4. WBS(진행중)

5. 데이터 전처리 결과서 (EDA)

6. 인공지능 학습 결과서

7. 수행결과(테스트 결과 화면 또는 시연 페이지)

8. 한 줄 회고
