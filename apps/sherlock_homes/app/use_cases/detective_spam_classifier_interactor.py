from __future__ import annotations

from sherlock_homes.app.dtos.detective_spam_classifier_dto import ClassifyCommand, ClassifyResult
from sherlock_homes.app.ports.input.detective_spam_classifier_use_case import SpamClassifierUseCase
from star_craft.domain.ontology.spam.spam_rules import classify_by_keywords


class SpamClassifierInteractor(SpamClassifierUseCase):

    def classify(self, command: ClassifyCommand) -> ClassifyResult:
        category = classify_by_keywords(command.text)
        return ClassifyResult(category=category)
