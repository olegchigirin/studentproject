import string
from random import choices


def get_slug(model_name: str) -> str:
    unique = get_random_string_ascii_lowercase()
    slug = '{}-{}'.format(model_name, unique)
    return slug


def get_random_string_ascii_lowercase(size: int = 8) -> str:
    result = ''.join(choices(string.ascii_lowercase, k=size))
    return result
