# Generated by Django 3.0.7 on 2020-07-16 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoopeasy', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
    ]
