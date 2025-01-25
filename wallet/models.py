from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    def add_balance(self, amount):
        """Método para adicionar saldo à carteira."""
        if amount > 0:
            self.balance += amount
            self.save()
        else:
            raise ValueError("O valor a ser adicionado deve ser positivo.")

class Transaction(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transactions', default=1)  # Substitua '1' pelo ID do usuário padrão
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transactions', null=True)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
