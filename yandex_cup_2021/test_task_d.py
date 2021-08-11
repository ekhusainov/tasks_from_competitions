import pytest

from task_d import (
    check_two_degree,
    building_dictionary_from_names,
    data_and_dict_to_sorted_frequency_count,
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


@pytest.mark.parametrize(
    "data, etalon_answer",
    [
        pytest.param(
            [
                "IVANOV PETROV",
                "PETROV BOSHIROV",
                "BOSHIROV IVANOV",
            ],
            {
                "IVANOV": 2,
                "PETROV": 2,
                "BOSHIROV": 2,
            },
        ),
        pytest.param(
            [
                "GORBOVSKII ABALKIN",
                "SIKORSKI KAMMERER",
                "SIKORSKI GORBOVSKII",
                "BYKOV IURKOVSKII",
                "PRIVALOV BYKOV",
                "GORBOVSKII IURKOVSKII",
                "IURKOVSKII KIVRIN",
            ],
            {
                "GORBOVSKII": 3,
                "ABALKIN": 1,
                "SIKORSKI": 2,
                "KAMMERER": 1,
                "BYKOV": 2,
                "IURKOVSKII": 3,
                "PRIVALOV": 1,
                "KIVRIN": 1,
            }
        ),
    ]
)
def test_building_dictionary_from_names(data, etalon_answer):
    current_answer = building_dictionary_from_names(data)
    assert dict(current_answer) == etalon_answer, (
        f"Wroing {data}"
    )


@pytest.mark.parametrize(
    "data_names, name_frequency, etalon_answer",
    [
        pytest.param(
            [
                "IVANOV PETROV",
                "PETROV BOSHIROV",
                "BOSHIROV IVANOV",
            ],
            {
                "IVANOV": 2,
                "PETROV": 2,
                "BOSHIROV": 2,
            },
            [
                (2, 2),
                (2, 2),
                (2, 2),
            ]
        ),
        pytest.param(
            [
                "GORBOVSKII ABALKIN",
                "SIKORSKI KAMMERER",
                "SIKORSKI GORBOVSKII",
                "BYKOV IURKOVSKII",
                "PRIVALOV BYKOV",
                "GORBOVSKII IURKOVSKII",
                "IURKOVSKII KIVRIN",
            ],
            {
                "GORBOVSKII": 3,
                "ABALKIN": 1,
                "SIKORSKI": 2,
                "KAMMERER": 1,
                "BYKOV": 2,
                "IURKOVSKII": 3,
                "PRIVALOV": 1,
                "KIVRIN": 1,
            },
            [
                (1, 2),
                (1, 2),
                (1, 3),
                (1, 3),
                (2, 3),
                (2, 3),
                (3, 3),
            ]
        ),
    ]
)
def test_data_and_dict_to_sorted_frequency_count(data_names, name_frequency, etalon_answer):
    current_asnwer = data_and_dict_to_sorted_frequency_count(
        data_names,
        name_frequency,
    )
    current_asnwer = sorted(current_asnwer)
    assert etalon_answer == current_asnwer, (
        f"{data_names}, {name_frequency}"
    )
