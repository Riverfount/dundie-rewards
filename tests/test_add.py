import pytest

from dundie.core import add
from dundie.database import connect, add_person, commit


@pytest.mark.unit
def test_add_movement():
    db = connect()
    pk = 'joe@doe.com'
    data = {'role': 'Salesman', 'dept': 'Sales', 'name': 'Joe Doe'}
    _, created = add_person(db, pk, data)
    assert created

    pk = 'jim@doe.com'
    data = {'role': 'Manager', 'dept': 'Management', 'name': 'Jim Doe'}
    _, created = add_person(db, pk, data)
    assert created
    commit(db)

    add(-30, email='joe@doe.com')
    add(90, dept='Management')

    db = connect()
    assert db['balance']['joe@doe.com'] == 470
    assert db['balance']['jim@doe.com'] == 190
