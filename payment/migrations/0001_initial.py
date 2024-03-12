# Generated by Django 5.0.1 on 2024-03-07 09:52

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('razorpay_order_id', models.CharField(max_length=50, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(default='INR', max_length=3)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('failed', 'Failed')], default='created', max_length=10)),
                ('receipt', models.CharField(blank=True, max_length=50, null=True)),
                ('offer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_due', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('attempts', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razorpay_payment_id', models.CharField(max_length=50, unique=True)),
                ('razorpay_signature', models.CharField(max_length=255)),
                ('payment_method', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='payment.ordermodel')),
            ],
        ),
    ]
