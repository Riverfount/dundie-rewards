import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_laod():
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_is_jim_halpert():
    """Test function load function"""
    assert load(PEOPLE_FILE)[0]['name'] == 'Jim Halpert'
