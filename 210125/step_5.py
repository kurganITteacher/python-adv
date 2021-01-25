import re

RE_EMAIL_VALIDATOR = re.compile(r'^[A-Za-z0-9._-]+@([a-z0-9._-]+\.)+[a-z]{2,}$')  # \n\r, .com .org .su


def email_is_valid(email):
    return RE_EMAIL_VALIDATOR.match(email)


assert email_is_valid('ivan@kss45.kpk.ru')
assert not email_is_valid('ivan@kss45.kpk.r')
assert not email_is_valid('ivan@kss45')
assert not email_is_valid('ivan@kss45.')
