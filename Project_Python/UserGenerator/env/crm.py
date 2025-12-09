"""Generator of random users"""

from faker import Faker
import logging
from pathlib import Path

fake = Faker()

basedir = Path(__file__).parent
logging.basicConfig(level=logging.DEBUG, filename=basedir / "user.log")

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Génération d'un utilisateur...")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(x):
    """Generate a list of users

    Args:
        x (int): number of users

    Returns:
        list[str]: users in list
    """
    logging.info(f"Génération de {x} utilisateur(s) en cours...")
    return [get_user() for _ in range(x)]
