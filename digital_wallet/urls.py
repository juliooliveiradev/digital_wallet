from django.urls import path
from wallet import views

urlpatterns = [
    path("", views.home_view, name="home"),  # Rota para a raiz
    path("login/", views.login_view, name="login"),
    path("create_user/", views.create_user_view, name="create_user"),
    path("add_balance/", views.add_balance_view, name="add_balance"),
    path(
        "transaction_history/",
        views.transaction_history_view,
        name="transaction_history",
    ),
    path("transfer_balance/", views.transfer_balance_view, name="transfer_balance"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
]
