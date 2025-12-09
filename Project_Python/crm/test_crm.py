from crm import User
import pytest
from tinydb import TinyDB, table
from tinydb.storages import MemoryStorage

@pytest.fixture
def setup_db():
    User.DB = TinyDB(storage=MemoryStorage)

@pytest.fixture
def user(setup_db):
    u = User(first_name="Patrick",
             last_name="Martin",
             phone_number="+1 234 567 890",
             address="123 Main Street")
    u.save()
    return u

def test_full_name(user):
    assert user.full_name == "Patrick Martin"


def test_exists(user):
    assert user.exists() is True


def test_db_instance(user):
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Patrick"
    assert user.db_instance["last_name"] == "Martin"
    assert user.db_instance["phone_number"] == "+1 234 567 890"
    assert user.db_instance["address"] == "123 Main Street"

def test_db_not_instance(setup_db):            #permet de tester une instance differente sans passer par la save
    u = User(first_name="Patrick",
             last_name="Martin",
             phone_number="+1 234 567 890",
             address="123 Main Street")
    assert u.db_instance is None


def test__check_phone_number(setup_db):
    user_good = User(first_name="Jean",
             last_name="Smith",
             phone_number="0123456789",
             address="10 rue par la-bas")
    user_bad = User(first_name="Jean",
             last_name="Smith",
             phone_number="abcde",
             address="10 rue par la-bas")
    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()

    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True


def test__check_names_empty(setup_db):
    user_bad = User(first_name="",
                    last_name="",
                    phone_number="0123456789",
                    address="10 rue par la-bas")

    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)


def test__check_names_invalid_characters(setup_db):
    user_bad = User(first_name="=)$*",
                    last_name="Martin&=*$",
                    phone_number="0123456789",
                    address="10 rue par la-bas")

    with pytest.raises(ValueError) as err:
        user_bad._check_names()

    assert "Nom invalide" in str(err.value)


def test_delete(setup_db):
    user_test = User(first_name="Patrick",
                     last_name="Martin",
                     phone_number="+1 234 567 890",
                     address="123 Main Street")
    user_test.save()
    first = user_test.delete()
    second = user_test.delete()
    assert isinstance(first, list)
    assert isinstance(second, list)
    assert len(first) > 0
    assert len(second) == 0


def test_save(setup_db):
    user_test = User(first_name="Patrick",
                     last_name="Martin",
                     phone_number="+1 234 567 890",
                     address="123 Main Street")
    user_test_double = User(first_name="Patrick",
                            last_name="Martin",
                            phone_number="+1 234 567 890",
                            address="123 Main Street")
    first = user_test.save()
    second = user_test_double.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1