import sys, os
import pytest

sys.path.append(os.getcwd())

from Exercise4 import max_max

stats = {
  'facebook': 55, 
  'yandex': 120, 
  'vk': 115, 
  'google': 99, 
  'email': 42, 
  'ok': 98}

def test_1():
    res = max_max(stats)
    assert res == 'yandex'



stats2 = {
  'facebook': 55, 
  'yandex': 120, 
  'vk': 115, 
  'google': 130, 
  'email': 42, 
  'ok': 98}

def test_2():
    res = max_max(stats2)
    assert res == 'google'


if __name__ == '__main__':
    pytest.main(['tests/test3.py'])
# python -m pytest tests\test2.py