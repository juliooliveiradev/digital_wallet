from django.test import TestCase
from django.contrib.auth.models import User
from wallet.models import Wallet, Transaction


class WalletTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.wallet = Wallet.objects.create(user=self.user, balance=100)

    def test_add_balance(self):
        self.wallet.add_balance(50)
        self.assertEqual(self.wallet.balance, 150)

    def test_transaction_creation(self):
        recipient = User.objects.create_user(username="recipient", password="password")
        transaction = Transaction.objects.create(
            sender=self.user, recipient=recipient, amount=50
        )
        self.assertEqual(transaction.amount, 50)
