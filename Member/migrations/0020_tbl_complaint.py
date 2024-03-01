# Generated by Django 5.0 on 2024-03-01 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_initial'),
        ('Member', '0019_tbl_weeklycollectionpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=50)),
                ('reply', models.CharField(max_length=50)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_memberadding')),
                ('relative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
            ],
        ),
    ]