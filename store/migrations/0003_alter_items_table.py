# Generated by Django 5.0 on 2024-01-11 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_member_items'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='items',
            table='items',
        ),
    ]