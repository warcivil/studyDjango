# Generated by Django 3.1.7 on 2021-05-03 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210503_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='kon_title',
        ),
    ]
