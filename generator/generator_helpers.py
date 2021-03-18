import random
import string
from datetime import date


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_date():
    return date(random.randrange(3000), random.randrange(1, 13), random.randrange(1, 32))
