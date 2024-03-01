# Generated by Django 5.0 on 2024-03-01 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_alter_tbl_electiondeclaration_podate'),
        ('FinanceHead', '0002_tbl_addloanname'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_monthlycollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_financehead')),
            ],
        ),
    ]
