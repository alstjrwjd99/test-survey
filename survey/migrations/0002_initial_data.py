from django.db import migrations


def create_survey_data_v1(apps, schema_editor):
    SurveyForm = apps.get_model('survey', 'SurveyForm')
    Question = apps.get_model('survey', 'Question')
    Choice = apps.get_model('survey', 'Choice')

    survey = SurveyForm.objects.create(
        title="모두닥 제품 및 서비스 만족도 조사",
        sub_title="고객님의 솔직한 의견을 남겨주시면 도움이 됩니다.",
        description="이 설문조사는 현재 코쿤의 개발 학습을 위해 진행됩니다.",
        message="참여해주셔서 감사합니다!"
    )

    question1 = Question.objects.create(
        survey_form=survey,
        title="전체적인 과제 만족도를 선택해주세요.",
        order=1,
        type='multiple_choice'
    )

    choices_q1 = ["매우 불만족", "불만족", "보통", "만족", "매우 만족"]
    for i, choice_text in enumerate(choices_q1):
        Choice.objects.create(question=question1, text=choice_text, order=i+1)

    Question.objects.create(
        survey_form=survey,
        title="개선이 필요한 부분이 있다면 자유롭게 작성해주세요.",
        order=2,
        type='text'
    )

    question2 = Question.objects.create(
        survey_form=survey,
        title="가장 유용했던 기능은 무엇인가요? (복수 선택 가능)",
        sub_title="여러 개를 선택할 수 있습니다.",
        order=3,
        type='checkbox'
    )

    choices_q2 = ["간편한 로그인 기능", "직관적인 UI 디자인", "빠른 데이터 로딩 속도", "다양한 필터링 옵션"]
    for i, choice_text in enumerate(choices_q2):
        Choice.objects.create(question=question2, text=choice_text, order=i+1)


def create_survey_data_v2(apps, schema_editor):
    SurveyForm = apps.get_model('survey', 'SurveyForm')
    Question = apps.get_model('survey', 'Question')
    Choice = apps.get_model('survey', 'Choice')

    survey = SurveyForm.objects.create(
        title="새로운 제품/기능 아이디어 설문조사",
        sub_title="여러분의 아이디어가 새로운 제품이 될 수 있습니다.",
        description="미래 서비스에 대한 아이디어를 공유해 주세요.",
        message="소중한 의견 감사합니다!"
    )

    Question.objects.create(
        survey_form=survey,
        title="새롭게 추가되었으면 하는 기능이 있나요?",
        order=1,
        type='text'
    )

    question2 = Question.objects.create(
        survey_form=survey,
        title="우리 제품을 얼마나 자주 사용하시나요?",
        order=2,
        type='multiple_choice'
    )
    choices_q2 = ["매일", "주 3~4회", "주 1~2회", "월 1~2회", "거의 사용하지 않음"]
    for i, choice_text in enumerate(choices_q2):
        Choice.objects.create(question=question2, text=choice_text, order=i+1)

    question2 = Question.objects.create(
        survey_form=survey,
        title="다음 중 관심 있는 분야를 모두 선택해주세요.",
        order=3,
        type='checkbox'
    )
    choices_q3 = ["AI 기술", "웹 개발", "모바일 앱", "데이터 분석", "클라우드 서비스", "UI/UX 디자인"]
    for i, choice_text in enumerate(choices_q3):
        Choice.objects.create(question=question2, text=choice_text, order=i+1)

    question3 = Question.objects.create(
        survey_form=survey,
        title="이용자 커뮤니티가 생긴다면 참여하시겠습니까?",
        order=4,
        type='multiple_choice'
    )
    choices_q4 = ["네, 적극적으로 참여하겠습니다.", "고민해 보겠습니다.", "아니오."]
    for i, choice_text in enumerate(choices_q4):
        Choice.objects.create(question=question3, text=choice_text, order=i+1)


class Migration(migrations.Migration):
    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_survey_data_v1),
        migrations.RunPython(create_survey_data_v2),
    ]
