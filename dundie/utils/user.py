from string import ascii_letters, digits
from random import sample


def generate_simple_password(size=8):
    return ''.join(sample(ascii_letters + digits, size))
