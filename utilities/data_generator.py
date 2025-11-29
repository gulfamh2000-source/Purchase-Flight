from faker import Faker

_fake = Faker()


def random_user():
    """
    Generate random dummy user data for purchase.
    """
    return {
        "name": _fake.name(),
        "email": _fake.email(),
        "phone": _fake.phone_number()
    }
