# Generated by Django 5.0.4 on 2024-04-14 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_charlesstudent_charlesoffense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charlesoffense',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.charlesstudent'),
        ),
    ]