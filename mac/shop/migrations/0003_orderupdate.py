# Generated by Django 3.2.5 on 2021-07-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210721_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
