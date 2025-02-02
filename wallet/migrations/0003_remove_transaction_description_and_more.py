# Generated by Django 5.1.5 on 2025-01-25 05:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wallet", "0002_remove_transaction_receiver_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="description",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="type",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="wallet",
        ),
        migrations.AddField(
            model_name="transaction",
            name="recipient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_transactions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="transaction",
            name="sender",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_transactions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="amount",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="wallet",
            name="balance",
            field=models.FloatField(default=0),
        ),
    ]
