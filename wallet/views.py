from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from wallet.models import Wallet, Transaction
from datetime import datetime


def home_view(request):
    if request.user.is_authenticated:
        return redirect(
            "dashboard"
        )  # Se o usuário estiver logado, redireciona para o dashboard
    else:
        return redirect(
            "login"
        )  # Se o usuário não estiver logado, redireciona para o login


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Credenciais inválidas!")
    return render(request, "login.html")


def create_user_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username, password=password)
                Wallet.objects.create(user=user, balance=0)  # Criação da carteira
                messages.success(request, "Conta criada com sucesso!")
                return redirect("login")
            else:
                messages.error(request, "Nome de usuário já existe!")
        else:
            messages.error(request, "As senhas não coincidem!")
    return render(request, "create_user.html")


@login_required
def dashboard_view(request):
    try:
        wallet = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        # Se não houver uma wallet para o usuário, cria uma nova
        wallet = Wallet.objects.create(user=request.user, balance=0)

    return render(request, "dashboard.html", {"wallet": wallet})


@login_required
def add_balance_view(request):
    if request.method == "POST":
        try:
            amount = float(request.POST.get("amount"))
            if amount <= 0:
                messages.error(request, "O valor deve ser positivo!")
                return redirect("add_balance")

            wallet = Wallet.objects.get(user=request.user)
            wallet.add_balance(
                amount
            )  # Usando o método add_balance para adicionar o valor
            messages.success(request, "Saldo adicionado com sucesso!")
        except Wallet.DoesNotExist:
            messages.error(request, "Erro ao encontrar a carteira do usuário!")
        except ValueError:
            messages.error(request, "Valor inválido!")

        return redirect("dashboard")
    return render(request, "add_balance.html")


@login_required
def transaction_history_view(request):
    # Obtendo os valores das datas de início e fim da requisição (se fornecidos)
    start_date = request.GET.get("start_date", None)
    end_date = request.GET.get("end_date", None)

    # Filtrando as transações de acordo com o usuário
    transactions = Transaction.objects.filter(
        sender=request.user
    ) | Transaction.objects.filter(recipient=request.user)

    # Aplicando os filtros de data, se fornecidos
    if start_date and end_date:
        transactions = transactions.filter(
            date__range=[start_date + " 00:00", end_date + " 23:59"]
        )

    # Processando as transações para adicionar o campo 'sender_or_recipient' para facilitar a exibição no template
    for transaction in transactions:
        if transaction.sender != request.user:
            transaction.sender_or_recipient = transaction.sender
            transaction.other_party = transaction.recipient
        else:
            transaction.sender_or_recipient = transaction.recipient
            transaction.other_party = transaction.sender

    return render(request, "transaction_history.html", {"transactions": transactions})


@login_required
def transfer_balance_view(request):
    if request.method == "POST":
        recipient_username = request.POST.get("recipient")
        amount = float(request.POST.get("amount"))
        try:
            recipient = User.objects.get(username=recipient_username)
            sender_wallet = Wallet.objects.get(user=request.user)
            recipient_wallet = Wallet.objects.get(user=recipient)

            if sender_wallet.balance >= amount:
                sender_wallet.balance -= amount
                recipient_wallet.balance += amount
                sender_wallet.save()
                recipient_wallet.save()

                # Criando uma transação
                Transaction.objects.create(
                    sender=request.user, recipient=recipient, amount=amount
                )
                messages.success(request, "Transferência realizada com sucesso!")
                return redirect("dashboard")
            else:
                messages.error(request, "Saldo insuficiente!")
        except User.DoesNotExist:
            messages.error(request, "Usuário destinatário não encontrado!")
    return render(request, "transfer_balance.html")


def logout_view(request):
    logout(request)
    return redirect("login")
