# Generated by Django 5.1.2 on 2024-11-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_signup_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Count_books',
            field=models.IntegerField(default=0),
        ),
    ]
