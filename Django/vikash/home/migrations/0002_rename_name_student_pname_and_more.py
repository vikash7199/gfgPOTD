# Generated by Django 4.2.2 on 2024-03-07 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='pname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Quantity',
            new_name='quantity',
        ),
    ]
