# Generated by Django 4.2.7 on 2023-12-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_remove_notepost_note_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='reaction_type',
            field=models.CharField(choices=[('OK', '見ました'), ('COMMENT', 'コメントあり')], max_length=20),
        ),
    ]