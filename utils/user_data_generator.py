from faker import Faker

fake = Faker()


def generate_user_data() -> dict:
    """
    Generates random user data for checkout using the Faker library.

    :return: A dictionary containing 'first_name', 'last_name', and 'postal_code'.
    """
    first_name = fake.first_name()
    last_name = fake.last_name()
    postal_code = fake.zipcode()
    return {
        "first_name": first_name,
        "last_name": last_name,
        "postal_code": postal_code,
    }