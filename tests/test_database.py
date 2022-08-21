import pytest

from dundie.database import EMPTY_DB, add_person, commit, connect, add_movement


@pytest.mark.unit
def test_database_schema():
    db = connect()
    assert db.keys() == EMPTY_DB.keys()


@pytest.mark.unit
def test_commit_to_database():
    db = connect()
    data = {
        'name': 'Joe Doe',
        'role': 'Salesman',
        'dept': 'Sales',
    }
    db['people']['joe@doe.com'] = data
    commit(db)

    db = connect()
    assert db['people']['joe@doe.com'] == data


@pytest.mark.unit
def test_add_person_for_the_first_time():
    pk = 'joe@doe.com'
    data = {
        'role': 'Salesman',
        'dept': 'Sales',
        'name': 'Joe Doe'
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created
    commit(db)

    db = connect()
    assert db['people'][pk] == data
    assert db['balance'][pk] == 500
    assert len(db['movement'][pk]) > 0
    assert db['movement'][pk][0]['value'] == 500


@pytest.mark.unit
def test_negative_add_person_invalid_mail():
    with pytest.raises(ValueError):
        add_person({}, ".@blah", {})


@pytest.mark.unit
def test_add_or_points_for_person():
    pk = 'joe@doe.com'
    data = {
        'role': 'Salesman',
        'dept': 'Sales',
        'name': 'Joe Doe'
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created
    commit(db)
    db = connect()
    before = db['balance'][pk]
    add_movement(db, pk, -100, "manager")
    commit(db)

    db = connect()
    after = db['balance'][pk]

    assert after == before - 100
    assert after == 400
    assert before == 500
