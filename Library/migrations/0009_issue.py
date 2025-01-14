# Generated by Django 5.1.2 on 2024-11-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0008_remove_book_count_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(max_length=15)),
                ('issue_date', models.DateField()),
                ('book_name', models.CharField(max_length=100)),
            ],
        ),
    ]
