# Generated by Django 2.2.16 on 2020-11-05 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samazon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
