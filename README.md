# test-survey
설문조사 모델 설계 테스트 용 레포지토리입니다.

## 테이블 구조
- User (id, name, ...)
- UserSubmit (id, User (FK), SurveyForm (FK), created)
- SurveyForm (id, title (not null), sub_title, description, message, ...)
- Question (id, SurveyForm(FK 1대다), title (not null), sub_title, order (not null), type, ...)
- Answer (id, UserSubmit(FK), Question (FK), Choice(FK), text, ... )
- Choice (id, Question (FK), text, order, ...)

<img width="4992" height="1760" alt="image" src="https://github.com/user-attachments/assets/17f5c8f8-ee81-4e03-8695-e9e8609b4bbd" />
