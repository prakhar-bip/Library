# Generated by Django 5.1.2 on 2024-11-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0005_rename_books_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='roles',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
