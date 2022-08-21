"""Core module of dundie. """
import os
from csv import reader

from dundie.database import connect, add_person, commit, add_movement
from dundie.utils.logger import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database."""
    try:
        csv_data = reader(open(filepath))
    except FileExistsError as e:
        log.error(str(e))
        raise e

    db = connect()
    people = []
    headers = ['name', 'dept', 'role', 'email']
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop('email')
        person, created = add_person(db, pk, person_data)
        return_data = person.copy()
        return_data['created'] = created
        return_data['email'] = pk
        people.append(return_data)
    commit(db)
    return people


def read(**query):
    """Read data from db and filters using query"""
    db = connect()
    return_data = []
    for pk, data in db['people'].items():

        if (dept := query.get('dept')) and dept != data['dept']:
            continue
        if (email := query.get('email')) and email != pk:
            continue

        return_data.append(
            {
                'email': pk,
                'balance': db['balance'][pk],
                'last_movement': db['movement'][pk][-1]['date'],
                **data
            }
        )
    return return_data


def add(value, **query):
    """Add value to each record on query"""
    people = read(**query)
    if not people:
        raise RuntimeError('Not Found')
    user = os.getenv('USER')
    db = connect()
    for person in people:
        add_movement(db, person['email'], value, user)
    commit(db)
