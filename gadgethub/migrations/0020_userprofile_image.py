# Generated by Django 4.1.3 on 2023-03-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0019_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]