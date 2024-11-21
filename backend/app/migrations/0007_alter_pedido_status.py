# Generated by Django 5.1.3 on 2024-11-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_pedido_data_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Aprovado', 'Aprovado'), ('Em produção', 'Em produção'), ('Em entrega', 'Em entrega'), ('Concluído', 'Concluído')], default='Pendente', max_length=150),
        ),
    ]