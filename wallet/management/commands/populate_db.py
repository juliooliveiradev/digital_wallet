from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from wallet.models import Wallet


class Command(BaseCommand):
    help = "Populates the database with test data"

    def handle(self, *args, **kwargs):
        username = "testuser"
        password = "password123"

        # Verifica se o usuário já existe ou o cria
        user, created = User.objects.get_or_create(
            username=username, defaults={"password": password}
        )

        # Verifica se a carteira já existe para o usuário ou a cria
        wallet, wallet_created = Wallet.objects.get_or_create(
            user=user, defaults={"balance": 1000.00}
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Usuário '{username}' criado com sucesso!")
            )
        else:
            self.stdout.write(self.style.WARNING(f"Usuário '{username}' já existe!"))

        if wallet_created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Carteira para o usuário '{username}' criada com sucesso!"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Carteira para o usuário '{username}' já existe!")
            )

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
