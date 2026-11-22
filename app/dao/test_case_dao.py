from typing import Optional
from app.models.test_case import TestCase

# In-memory store
_test_cases: dict[str, TestCase] = {}


def save(test_case: TestCase) -> TestCase:
    _test_cases[test_case.id] = test_case
    return test_case


def find_by_id(test_case_id: str) -> Optional[TestCase]:
    return _test_cases.get(test_case_id)


def find_all() -> list[TestCase]:
    return list(_test_cases.values())
