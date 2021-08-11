import pytest

from task_d import (
    check_two_degree,
)

@pytest.mark.parametrize(
    "number, etalon_answer",
    [
        pytest.param(16, True),
        pytest.param(32, True),
        pytest.param(8, True),
        pytest.param(2, True),
        pytest.param(1, True),
        pytest.param(15, False),
        pytest.param(18, False),
        pytest.param(1024, True),
        pytest.param(1111, False),
    ]
)
def test_check_two_degree(number, etalon_answer):
    current_answer = check_two_degree(number)
    assert etalon_answer == current_answer, (
        f"{number} is not {current_answer}"
    )