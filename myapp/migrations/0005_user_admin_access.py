# Generated by Django 4.2.3 on 2023-08-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin_access',
            field=models.BooleanField(default=False),
        ),
    ]
