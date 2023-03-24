# Generated by Django 4.1.7 on 2023-03-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='games_played',
            new_name='blitz',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='rating',
            new_name='classical',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='country',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='player',
            name='username',
        ),
        migrations.RemoveField(
            model_name='player',
            name='win_percent',
        ),
        migrations.AddField(
            model_name='player',
            name='rapid',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
