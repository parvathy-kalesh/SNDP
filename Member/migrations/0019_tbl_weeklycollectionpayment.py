# Generated by Django 5.0 on 2024-03-01 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceHead', '0004_tbl_weeklycollection'),
        ('Guest', '0003_initial'),
        ('Member', '0018_tbl_monthlycollectionpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_weeklycollectionpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_memberadding')),
                ('relative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
                ('weeklycollection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceHead.tbl_weeklycollection')),
            ],
        ),
    ]
