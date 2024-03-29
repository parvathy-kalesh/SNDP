# Generated by Django 5.0 on 2024-01-27 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_alter_tbl_electiondeclaration_podate'),
        ('Guest', '0003_initial'),
        ('Member', '0005_delete_tbl_scholarshipapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_scholarshipapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('document', models.FileField(upload_to='MemberDocs/')),
                ('date', models.DateField()),
                ('member_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_memberadding')),
                ('relative_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Member.tbl_relatives')),
                ('scholarship_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_scholarshipname')),
            ],
        ),
    ]
