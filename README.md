# test-survey
설문조사 모델 설계 테스트 용 레포지토리입니다.

## 테이블 구조
- User (id, name, ...)
- UserSubmit (id, User (FK), SurveyForm (FK), created ...)
- SurveyForm (id, title (not null), sub_title, description, message, ...)
- Question (id, SurveyForm(FK 1대다), title (not null), sub_title, order (not null), type, ...)
- Answer (id, UserSubmit(FK), Question (FK), Choice(FK), text, ... )
- Choice (id, Question (FK), text, order, ...)

<img width="5168" height="1760" alt="image" src="https://github.com/user-attachments/assets/32ba6d63-b3d8-4d3a-84f0-17ccbf1c6326" />

### 설명
1. 한 명의 유저는 여러 설문조사를 제출할 수 있으며, 하나의 설문조사에는 여러 유저가 응답할 수 있습니다. UserSubmit 테이블은 이 관계를 연결합니다.
2. 설문조사 폼은 각 제출마다 변경이 될 수 있습니다.
3. 설문조사 폼에는 질문 - 대답의 방식으로 이루어져 있으며 각각 Answer은 주관식 대답, Choice는 객관식 대답이 됩니다.
4. 기타를 선택한 경우 짧은 주관식 응답을 받는 객관식은 Choice 테이블의 기타 옵션에 들어가며, Answer 테이블의 text에 저장이 됩니다.
5. 응답 타입은 추가는 별도의 테이블 생성을 고려했으나 파일 추가, 오디오 추가 등과 같은 경우는 제외하여 ENUM type을 활용합니다.
