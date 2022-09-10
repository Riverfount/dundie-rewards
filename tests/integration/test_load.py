import pytest
from click.testing import CliRunner

from dundie.cli import load, main
from tests.constants import PEOPLE_FILE

cmd = CliRunner()


@pytest.mark.integration
@pytest.mark.medium
def test_postive_load():
    """Test command load."""
    out = cmd.invoke(load, PEOPLE_FILE)
    assert 'Dunder Mifflin Associates' in out.output


@pytest.mark.parametrize('wrong_command', ['loady', 'carrega', 'start'])
def test_negative_load(wrong_command):
    out = cmd.invoke(main, wrong_command, PEOPLE_FILE)
    assert out.exit_code != 0
    assert f"No such command '{wrong_command}'." in out.output
