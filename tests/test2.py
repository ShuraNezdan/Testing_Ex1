import sys, os
import pytest

sys.path.append(os.getcwd())

from Exercise3 import percent

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
def test_1():
    res = percent(queries)
    assert res[3] > 50


queries2 = [
    'смотреть онлайн',
    'новости кино',
    'афиша кино',
    'курс доллара',
    'сериалы летом',
    'курс питону',
    'сериалы спорт'
    ]
def test_2():
    res = percent(queries2)
    assert res[2] == 100


if __name__ == '__main__':
    pytest.main(['tests/test2.py'])
# python -m pytest tests\test2.py