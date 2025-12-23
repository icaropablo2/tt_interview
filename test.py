import pytest

from venmo_exceptions import UsernameException,PaymentException
from user import User
from main import MiniVenmo

def test_user_payment():
    # this method don't allow me to test
    minivenmo = MiniVenmo()
    minivenmo.run()

def test_user_payment__():
    minivenmo = MiniVenmo()
    bobby = minivenmo.create_user("Bobby", 0, "4111111111111111")
    carol = minivenmo.create_user("Bobby", 10, "4242424242424242")

    with pytest.raises(PaymentException) as error:
        payment = bobby.pay(carol, 5.00, "Coffee")
    assert str(error) == "<ExceptionInfo PaymentException('User cannot pay themselves.') tblen=3>"

