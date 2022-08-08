import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.high
def test_laod():
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'J'