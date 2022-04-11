# Generated by Django 3.2.4 on 2022-01-30 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0010_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='clien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField(default=0)),
                ('client_name', models.CharField(max_length=50)),
                ('client_address', models.CharField(max_length=50)),
                ('client_phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('transportation', models.CharField(max_length=50)),
                ('distribution_id', models.CharField(default=0, max_length=20)),
                ('client_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('deadline', models.DateField()),
                ('client_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='gnpps.clien')),
            ],
        ),
    ]