# Generated by Django 4.2.1 on 2023-06-01 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solution', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog',
            new_name='Blog',
        ),
    ]
