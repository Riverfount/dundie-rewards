import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_laod():
    assert len(load(PEOPLE_FILE)) == 3
    assert load(PEOPLE_FILE)[0][0] == 'J'
