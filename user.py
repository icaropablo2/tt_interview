import re
from venmo_exceptions import UsernameException, CreditCardException, PaymentException
from payment import Payment

class User:

    feed = {}

    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')


    def retrieve_feed(self, username):
        # TODO: add code here
        return self.feed.get(username) or []

    def add_friend(self, new_friend):
        # TODO: add code here
        pass

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException('Invalid credit card number.')

    def pay(self, target, amount, note):
        # TODO: add logic to pay with card or balance
        actor = self
        payment = Payment(amount, actor, target, note)

        if self.balance >= amount:
            self.pay_with_balance(target, amount, note)
        else:
            self.pay_with_card(target, amount, note)
        
        self._add_feed(payment)
        
        return payment

    def _add_feed(self, payment):
        actor_name = payment.actor.username
        if not self.feed.get(actor_name):
            self.feed[actor_name] = []
        self.feed[actor_name].append(payment)

    def pay_with_card(self, target, amount, note):
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')

        elif amount <= 0.0:
            raise PaymentException('Amount must be a non-negative number.')

        elif self.credit_card_number is None:
            raise PaymentException('Must have a credit card to make a payment.')

        self._charge_credit_card(self.credit_card_number)
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def pay_with_balance(self, target, amount, note):
        # TODO: add code here
        if self.balance < amount:
            raise PaymentException('Without found to make this payment.')

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')

        target.add_to_balance(amount)

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass