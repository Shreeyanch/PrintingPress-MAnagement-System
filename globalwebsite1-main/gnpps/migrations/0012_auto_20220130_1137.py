# Generated by Django 3.2.4 on 2022-01-30 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0011_clien_distribution_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='client_id1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='gnpps.clien'),
        ),
        migrations.AddField(
            model_name='order',
            name='client_id1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='gnpps.clien'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client_id',
            field=models.CharField(max_length=50),
        ),
    ]
