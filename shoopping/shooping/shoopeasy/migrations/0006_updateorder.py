# Generated by Django 3.0.7 on 2020-07-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoopeasy', '0005_order_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateOrder',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
