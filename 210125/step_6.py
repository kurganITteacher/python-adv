import re

# dd.mm.yyyy
# RE_DATA_VALIDATOR = re.compile(r'^[0-9]{2}\.[0-9]{2}\.[0-9]{4}$')
# RE_DATA_VALIDATOR = re.compile(r'^([0-9]{2}\.){2}[0-9]{4}$')
RE_DATA_VALIDATOR = re.compile(r'^(\d{2}\.){2}\d{4}$')


def data_is_valid(data):
    return RE_DATA_VALIDATOR.match(data)


assert data_is_valid('25.01.2021')
assert not data_is_valid('5.01.2021')
assert not data_is_valid('05.01.21')
assert not data_is_valid('05,01,2021')
