# Generated by Django 3.2.4 on 2021-06-02 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Mean Boss', max_length=60)),
                ('health', models.IntegerField(default=100)),
            ],
        ),
    ]
