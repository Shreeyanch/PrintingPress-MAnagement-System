# Generated by Django 3.2.4 on 2021-08-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0009_auto_20210812_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField(max_length=2000)),
            ],
        ),
    ]
