# Generated by Django 4.1.3 on 2023-03-31 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0032_product_issaved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]