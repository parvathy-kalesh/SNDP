# Generated by Django 5.0 on 2024-03-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0013_alter_tbl_electiondeclaration_podate'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
