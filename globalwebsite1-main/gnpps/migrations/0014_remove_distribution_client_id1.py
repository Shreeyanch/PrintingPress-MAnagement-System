# Generated by Django 3.2.4 on 2022-01-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0013_auto_20220130_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distribution',
            name='client_id1',
        ),
    ]