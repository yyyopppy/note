# Generated by Django 4.2.7 on 2023-12-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_comment_delete_reaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
