from sherlock_homes.app.dtos.detective_spam_classifier_dto import ClassifyCommand
from sherlock_homes.app.use_cases.detective_spam_classifier_interactor import SpamClassifierInteractor
from star_craft.domain.ontology.spam.spam_category import SpamCategory


def test_classify_detects_phishing():
    interactor = SpamClassifierInteractor()
    result = interactor.classify(ClassifyCommand(text="계정 확인이 필요합니다 login now"))
    assert result.category == SpamCategory.PHISHING


def test_classify_defaults_to_legitimate():
    interactor = SpamClassifierInteractor()
    result = interactor.classify(ClassifyCommand(text="내일 점심 같이 먹어요"))
    assert result.category == SpamCategory.LEGITIMATE
