# Generated by Django 4.1.1 on 2022-11-24 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monay', '0005_remove_cliente_emailconf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='fotoCliente',
        ),
    ]
