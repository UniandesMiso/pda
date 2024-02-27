from werkzeug.exceptions import HTTPException

from contracts.seedwork.domain.rules import BusinessRule


class DomainException(HTTPException): ...


class BusinessRuleException(DomainException):

    def __init__(self, rule: BusinessRule):
        self.code = 400
        self.description = rule.error()
