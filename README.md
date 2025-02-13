# SKN09-2nd-4Team

> SK Networks AI Camp 9기
> 
> 개발기간: 25.02.03 - 25.02.14
<br>

# 0. Team Introduction (팀 소개)

## 👑팀명: MVP ("Million Vault Protector") 

![Image](https://github.com/user-attachments/assets/92e589e1-f3ea-447d-94a4-3aeb6625956a)
<br>

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

# 1. Project Introduction (프로젝트 개요)

## 프로젝트 명
- **👑MVP👑**: 데이터 기반 ABC 은행 가입고객 이탈자 분석 및 예측

### 목표
- 본 프로젝트는 데이터 분석 및 머신러닝을 활용하여 ABC 은행 고객의 이탈 가능성을 예측하는 모델을 개발하는 것입니다.
- 이를 통해 ABC 은행은 고객 이탈을 사전에 감지하고, 맞춤형 마케팅 전략을 수립하여 고객 유지율을 높일 수 있을 것입니다.

### 프로젝트 배경

![image](https://github.com/user-attachments/assets/cb482edb-53a0-40a9-a7d1-17ef4e1a8a18)

- 현대 금융 시장에서 고객 유지는 은행 및 금융 기관의 지속 가능한 성장을 위해 필수적인 요소입니다. 그러나 현대의 전통적인 은행의 마케팅 비용은 증가한 반면에, 고객은 오히려 이탈하는 상황에 직면했습니다. 또한 시중 은행에 대한 고객 충성도 역시시 하락하는 경향을 보입니다.
<br>

![image](https://github.com/user-attachments/assets/3a3ecd71-6f16-42f6-b811-c7069a9588a7)

- Harvard Business Review Reprint-"The Economics of E-Loyalty" (2002) by Frederick F. Reichheld & Phil Schefte-에 따르면, 기존 고객을 유지하는 비용은 신규 고객을 유치하는 비용보다 5배 저렴하다고 알려져 있습니다. 따라서, 기존 고객의 이탈을 방지하는 것이 운영 비용 절감 및 수익성 강화에 효과적인 전략이 될 수 있습니다.
<br>

  ![image](https://github.com/user-attachments/assets/fd4d2a7e-0580-43ca-9aed-375a82904b1f)

- 하지만 Sage Journal-Reducing Adverse Selection through Customer Relationship Management
Yong Cao and Thomas S. Gruca-에 따르면, 많은 금융 기관은 고객 이탈이 발생한 후에 대응하는 사후 관리 방식에 의존하고 있어 실질적인 비용 절감과 고객 유지 효과를 극대화하는 데 어려움을 겪고 있습니다. 이에 따라, 사전적으로 고객 이탈을 예측하고 선제적으로 대응할 수 있는 데이터 기반의 고객 이탈 예측 모델이 필요하게 되었습니다.

### 분석 및 접근 방법
- 데이터 수집: 고객의 신용점수, 근속년수, 이용 상품개수, 활동 여부 패턴 등 ABC 은행의 데이터셋을 활용
- 데이터 전처리 및 시각화: 결측치 및 이상치 확인, 데이터 정규화 등의 과정을 수행
- 특성 엔지니어링: 고객 연령, 소득 수준, 신용 점수, 계좌 잔액, 이용 국가, 성별 등의 중요한 특성 추출
- 모델 사용: XGBoost, RandomForest, CatBoost, AdaBoost 등 다양한 머신러닝 알고리즘을 적용하여 예측 성능 비교 분석
- 모델 평가: 상위 4개 모델에 대한 앙상블을 적용하여 정확도, 정밀도, 재현율, F1-score 및 ROC-AUC 등의 성능 지표를 활용한 모델 고도화

### 기대 효과
- 고객 이탈 사전 예방: 이탈 가능성이 높은 고객을 조기에 발견하여 맞춤형 프로모션 및 상담 제공
- 비용 절감: 고객 유지 비용 절감 및 신규 고객 유치 비용 최소화
- 비즈니스 성장: 데이터 기반 의사결정을 통한 ABC 은행의 경쟁력 강화 및 고객 만족도 향상

### 요약
- 본 프로젝트를 통해 전통적인 은행의 고객 이탈 문제를 보다 효과적으로 해결하고, 장기적인 고객 관계 관리를 강화할 수 있습니다.
- 데이터 기반의 예측 모델을 활용하여 고객 맞춤형 전략을 수립함으로써 ABC 은행의 지속 가능한 성장을 도모하는 것이 본 프로젝트의 최종 목표입니다.
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
<br>

# 4. 데이터 전처리 결과서 (EDA)

### 데이터 수집 및 선정
> ![image](https://github.com/user-attachments/assets/eeb3c472-010d-41ef-94ec-71f1626159ba)
>- 출처: https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset
<br>

### 데이터 전처리 

> **1) 데이터 내용 확인**
>
>![Image](https://github.com/user-attachments/assets/5320d17c-6150-4db4-9222-68cb717fba02)
>
>
>
>
>- 포함된 주요 변수: credit_score (신용 점수), country (국가), age (나이), tenure (가입 기간), churn (이탈 여부) 등의 주요 변수
>
>- 데이터 크기 및 형태: 총 10000명의 고객 데이터, 12개의 변수 (2개의 object형 변수, 8개의 int형 변수, 2개의 float형 변수)
>
> **2) 결측치 확인**
>
>![Image](https://github.com/user-attachments/assets/51f85bf6-2824-4b7b-a28c-434d9914b3a7)
>
>- 결측치 확인결과 결측치 없음 확인
>
>**3) 이상치 확인**
>
>![Image](https://github.com/user-attachments/assets/dd1cd53f-0987-47e0-883c-1e69532c10c3)
>
>- 이상치 확인 결과, age(나이) 컬럼에서 이상치가 발견되었지만, 검토한 결과 고령 고객들의 나이가 높은 것으로 확인되었음. 따라서 별도의 조치는 취하지 않았음.
>
>**4) 데이터 시각화**
>
>**4-1) 전체 컬럼별 고객 이탈율과 전체 비율을 그래프로 시각화 및 확인**
>![Image](https://github.com/user-attachments/assets/50010858-bfdc-462e-adaf-91d9d99ef55c)
>
>**4-2) 각 컬럼별 고객 이탈률 및 고객 분포를 그래프로 시각화 및 확인**
>
>![Image](https://github.com/user-attachments/assets/800c94ce-3527-444b-83ef-a9796548e74d)
>- 독일의 고객 이탈율(32.44%)이 가장 높고, 프랑스(16.15%)와 스페인(16.67%)은 유사한 수준이지만 실제 고객 수는 프랑스가 가장 많은 것으로 나타남
> 
>![Image](https://github.com/user-attachments/assets/453e84ed-d593-43a3-82ff-45d20984d04d)
>- 신용등급에 따른 분류로는 각 이탈율이 비슷했지만, 실제 분포를 확인해본 결과 실제 고객 수는 신용등급이 중위권인 고객이 가장 많은것으로 나타남
>
>![Image](https://github.com/user-attachments/assets/452e73bb-9e95-4cff-a2fa-536a8fc3a1b8)
>- 성별에 따른 분류로는 여성(25.07%)의 이탈률이 남성(16.46%)보다 높았지만 실제 고객 수를 확인해본 결과 남성의 고객 수가 더 많은것으로 나타남
>
>![Image](https://github.com/user-attachments/assets/7d11f50c-7e7a-42a5-bdb2-660dccc7dbce)
>- 가입 상품의 개수에 따른 분류로는 4개 이상 가입고객의 이탈율이(100%)로 전원 이탈했지만, 실제 고객 수는 대부분이 1~2개의 상품에 가입한 것으로 나타남
>
>
>![Image](https://github.com/user-attachments/assets/9851172e-cd92-4835-8348-d3cfb9478a32)
>- 연령에 따른 분류로는 중년층(39.65%)의 이탈률이 가장 높으나, 실제 고객수는 청년의 비율이 가장 높은 것으로 나타남
>
>
>**4-3) 히트맵 시각화를 통한 컬럼별 상관관계 확인**
>![Image](https://github.com/user-attachments/assets/28f5a9f3-7c29-40ff-ad42-420e85616bb5)
>
> 양의 상관관계 중에서는 연령에 따른 이탈율이 가장 강했고, 음의 상관관계 중에서는 활동여부에 따른 이탈율이 가장 강했음
>
>**4-4) 이탈여부에 따른 컬럼별 중요도 확인**
>
>![Image](https://github.com/user-attachments/assets/3283f5f1-5ec9-4a4c-9ee9-16f357b34892)
>
> 히트맵을 bar plot으로 도식화하여 상관관계를 비교하기 편하게 하였음
>
>**4-5) 데이터 왜도확인 및 변환**
>
>![Image](https://github.com/user-attachments/assets/4f2aa2ed-57e5-46e4-ba7e-4359016b394a)
>
>![Image](https://github.com/user-attachments/assets/046ad368-bdde-41d3-8bc8-7d1c4345f9e1)
>
>![Image](https://github.com/user-attachments/assets/baceee0e-0bf1-4d1d-a90f-ff20d8b4c6b5)
>
>![Image](https://github.com/user-attachments/assets/4f8e096c-5d26-4f80-9b85-ec48bebf6801)
>
> - 왜도를 확인한 결과 Age 컬럼의 왜도가 1이 넘는것을 확인, Log 변환 처리과정을 거침
>
>**4-6) 추가분석과정**
>
>6-1) 범주형 데이터 간의 관계 시각화
>![Image](https://github.com/user-attachments/assets/649c2baa-eade-435b-8c96-241dfe2d4eb1)
>
>6-2) 이탈자와 활동인원 간의 관계 시각화
>![Image](https://github.com/user-attachments/assets/9ac4c885-33c2-4aef-9121-6c074298cc8e)
>
>**결론: 데이터셋의 비선형성 및 age 컬럼의 왜도가 1이 넘는 것을 확인. 또한 각 feature와 이탈율간의 상관관계에 따른 중요도 파악.**
<br>

# 5. 인공지능 학습 결과서
- 데이터셋 전처리 과정: 데이터셋 시각화에 따른 비선형 데이터셋 처리를 위해 Log 변환과 StandardScaler 과정을 거침. 다만, 전체 데이터셋 중 target의 비율이 약 20%에 해당되어 over-sampling 처리는 하지 않음.
- ML 선택 이유: 본 데이터셋은 1만 개의 row와 12개의 column을 가진 적은 규모의 데이터셋임. 따라서 DL을 활용할 경우 overfitting의 가능성이 우려되어 ML을 선택하였음.
- ML 모델 선택 이유: 해당 ABC 은행의 비선형 데이터셋에 최적화된 ensemble 모델을 목표로 11개의 ML 모델의 분석결과 지표 중 분류성능이 뛰어난 4개의 상위 모델을 선별하였음. 조합 방식은 선별된 네 개의 모델 중, boost 모델이 세 개가 포함되어 stacking이 제일 적절하다고 판단함.
- 학습된 인공지능 모델: XGBoost(Base), RandomForest(Base), CatBoost(Base), AdaBoost(Meta, Base) -> Ensemble Model (Stacking)
<br>

# 6. 수행결과 (테스트 결과 화면 또는 시연 페이지)
>
> Streamlit으로 시연
>
<br>

# 7. 한 줄 회고
- 박유진: Logistic regression, KNN 모델의 성능을 개선하기 위해 직접 grid search, log 변환, optuna 등을 적용해보면서 전처리의 중요성과 각 모델의 하이퍼파라미터에 대해 더 잘 이해할 수 있었다.  
- 서예찬: 이번 프로젝트를 하면서 EDA,ML과정에서 부족한 부분을 팀원들에게 많이 배웠고, 특히 ML과정에서 예전에는 써보지않았던 optuna 등을 적용하며 하이퍼파라미터 조정등을 통해 머신의 성능을 높이는 과정에 대해 이해도가 높아진것같다.
- 조이현: EDA 과정에서 범주형 데이터 컬럼별로 분류했을때, 이탈율 간의 상관계수 편차가 큰 것을 확인했다. 따라서, 각각의 최적화된 머신러닝을 튜닝하는 것까지 시도해보고 싶었지만, 앙상블 모델의 스태킹에 있어서 메타 모델과 베이스 모델의 예외적인 중복 설계를 새로이 발견하고 전체 데이터셋에 적용하는 시행착오를 겪은 결과, 시간적 여건이 되지 않아 심화 분석에 따른 머신러닝 최적화를 하지 못해 아쉬울 따름이다.
- 허정윤: 앙상블 모델을 보팅이나 스태킹으로 또 앙상블을 시키는 작업이 가능하단 걸 깨달았다. 예측 목적에 따라서 각 평가 지표들의 중요성이 달라진다는걸 깨달았다. 특히 고객 이탈의 경우 재현율이 중요하지만 정밀도가 너무 낮아지면 기존 고객을 잃을 수 있다.
<br>

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
