# Generated by Django 2.2 on 2021-11-30 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='following',
            name='check_that_dont_follow_yourself',
        ),
    ]
