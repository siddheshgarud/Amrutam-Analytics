# Generated by Django 4.0.3 on 2022-03-14 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_rename_status_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Total',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
