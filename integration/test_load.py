from subprocess import check_output

import pytest


@pytest.mark.medium
def test_load():
    """Test commando load."""
    out = check_output(
        ['dundie', 'load', 'tests/assets/people.csv']
    ).decode('utf-8').split('\n')
    assert len(out) == 2
