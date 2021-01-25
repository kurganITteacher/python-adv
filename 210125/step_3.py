alphabet = {chr(el) for el in range(ord('a'), ord('z') + 1)}
alphabet.update([chr(el) for el in range(ord('A'), ord('Z') + 1)])
alphabet.update([chr(el) for el in range(ord('0'), ord('9') + 1)])
alphabet.update(['@', '-', '.', '_'])

required_alphabet = {'@', '.'}


def email_is_valid(email):
    email_as_set = set(email)
    if not email or email_as_set - alphabet or required_alphabet - email_as_set:
        return False

    address, domain = email.split('@')
    domain_chunks = domain.split('.')
    if len(domain_chunks) < 2 or len(domain_chunks[-1]) < 2:
        return False

    return True


assert email_is_valid('ivan@kss45.kpk.ru')
assert not email_is_valid('ivan@kss45')
assert not email_is_valid('ivan@kss45.')
