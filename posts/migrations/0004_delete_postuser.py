# Generated by Django 2.2 on 2020-05-14 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostUser',
        ),
    ]
