import sys, os
import pytest

sys.path.append(os.getcwd())

from Exercise1 import rus



@pytest.mark.parametrize(
    'param, result', [
    ([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
], 6),
                     ([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']}
], 2)
])
def test_ex1_1(param, result):
    res = rus(param)
    assert len(res) == result


@pytest.mark.parametrize(
    'param', [
    ([
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
]),
                     ([
    {'visit1': ['Архангельск', 'Россия']},
    {'visit2': ['Курск', 'Россия']}
])
])
def test_ex1_2(param):
    res = rus(param)
    index = res[0]
    assert 'Россия' in index['visit1']


if __name__ == '__main__':
    pytest.main(['tests/test1.py'])
# python -m pytest tests\test1.py