# Generated by Django 5.0 on 2024-01-03 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_financehead'),
        ('FinanceHead', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addloanname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=50)),
                ('loan_details', models.CharField(max_length=50)),
                ('head', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_financehead')),
                ('loan_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_loan')),
            ],
        ),
    ]
