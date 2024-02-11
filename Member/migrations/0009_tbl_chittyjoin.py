# Generated by Django 5.0 on 2024-01-27 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_alter_tbl_electiondeclaration_podate'),
        ('FinanceHead', '0002_tbl_addloanname'),
        ('Guest', '0003_initial'),
        ('Member', '0008_alter_tbl_scholarshipapply_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_chittyjoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='MemberDocs/')),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('chittydata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinanceHead.tbl_chitty')),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_memberadding')),
                ('proof_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_proof')),
                ('relative_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
            ],
        ),
    ]
