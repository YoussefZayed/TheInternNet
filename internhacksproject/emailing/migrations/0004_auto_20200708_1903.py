# Generated by Django 3.0.7 on 2020-07-08 23:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emailing', '0003_auto_20200708_1830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailsent',
            old_name='Template',
            new_name='template',
        ),
        migrations.RemoveField(
            model_name='emailsent',
            name='company',
        ),
        migrations.RemoveField(
            model_name='emailsent',
            name='first_Name',
        ),
        migrations.RemoveField(
            model_name='emailsent',
            name='last_Name',
        ),
        migrations.AddField(
            model_name='emailsent',
            name='content',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailsent',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]