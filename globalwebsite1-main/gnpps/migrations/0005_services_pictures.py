# Generated by Django 3.2.4 on 2021-08-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnpps', '0004_alter_services_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='pictures',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to='img/%y'),
        ),
    ]
