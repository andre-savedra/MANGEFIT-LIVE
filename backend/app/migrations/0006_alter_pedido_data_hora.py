# Generated by Django 5.1.3 on 2024-11-20 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_salada_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_hora',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]