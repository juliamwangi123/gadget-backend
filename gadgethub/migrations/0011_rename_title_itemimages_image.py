# Generated by Django 4.1.3 on 2023-03-21 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0010_remove_itemimages_image_itemimages_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemimages',
            old_name='title',
            new_name='image',
        ),
    ]