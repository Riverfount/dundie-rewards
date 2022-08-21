import pytest

from dundie.core import read
from dundie.database import connect, add_person, commit


@pytest.mark.unit
def test_read_with_query():
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

    respnse = read()
    assert len(respnse) == 2

    response = read(dept='Management')
    assert len(response) == 1
    assert response[0]['name'] == 'Jim Doe'

    response = read(email='joe@doe.com')
    assert len(response) == 1
    assert response[0]['name'] == 'Joe Doe'
