# Generated by Django 4.1.3 on 2023-03-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgethub', '0029_alter_order_totalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='orderItemNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
