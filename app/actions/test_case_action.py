import uuid
from app.models.test_case import TestCase, TestCaseCreate
from app.dao import test_case_dao


def create_test_case(payload: TestCaseCreate) -> TestCase:
    test_case = TestCase(
        id=str(uuid.uuid4()),
        name=payload.name,
        description=payload.description,
    )
    return test_case_dao.save(test_case)


def get_test_case(test_case_id: str) -> TestCase | None:
    return test_case_dao.find_by_id(test_case_id)


def get_all_test_cases() -> list[TestCase]:
    return test_case_dao.find_all()
