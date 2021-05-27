# Подробнее про параметры xfail:
# https://docs.pytest.org/en/latest/reference/reference.html?highlight=xfail#pytest.mark.xfail

import pytest

# когда xfail проходит успешно - кидает ошибку
@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False